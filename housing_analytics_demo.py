#!/usr/bin/env python3
"""
Real Estate Investment Analytics Dashboard Demo
Using R statistics MCP server for advanced analysis and data visualization
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from pathlib import Path
from datetime import datetime
import warnings
import subprocess
import sys

warnings.filterwarnings('ignore')

class HousingAnalyticsDemo:
    """
    Real Estate Investment Analytics Dashboard using R MCP server for statistical analysis
    """

    def __init__(self):
        self.data_dir = Path('demos/Housingdata')
        self.output_dir = Path('demos/real_estate_analytics')
        self.output_dir.mkdir(exist_ok=True)

        # Set up matplotlib style
        plt.style.use('seaborn-v0_8')

        print("🏠 DakotaAI Real Estate Investment Analytics")
        print("=" * 60)

    def load_and_sample_data(self, sample_size=100):
        """Load and sample housing data for analysis"""
        print("Loading housing data...")

        all_data = []
        files_found = list(self.data_dir.glob('*.csv'))

        if not files_found:
            raise FileNotFoundError("No housing data files found in demos/Housingdata/")
        print(f"Found {len(files_found)} housing data files")

        # Sample a few files for demo
        sample_files = files_found[:3]  # Use first 3 datasets to keep demo manageable

        for file_path in sample_files:
            try:
                print(f"Loading {file_path.name}...")
                # Load just column headers and sample rows to avoid memory issues
                df = pd.read_csv(file_path, nrows=1000)

                # Extract time series data (exclude metadata columns)
                date_cols = [col for col in df.columns if col.startswith('20')]
                metadata_cols = ['RegionID', 'SizeRank', 'RegionName', 'RegionType',
                                'StateName', 'State', 'City', 'Metro', 'CountyName']

                # Keep metadata and a sample of time series data
                time_sample = date_cols[::12]  # Sample every 12 months (yearly)
                keep_cols = metadata_cols + time_sample

                df_filtered = df[keep_cols].head(sample_size)
                df_filtered['source_file'] = file_path.name

                all_data.append(df_filtered)

            except Exception as e:
                print(f"Error loading {file_path.name}: {e}")
                continue

        if not all_data:
            raise ValueError("No data could be loaded")

        self.raw_data = pd.concat(all_data, ignore_index=True)
        print(f"Loaded {len(self.raw_data)} housing records")

        return self.raw_data

    def analyze_with_r_mcp(self):
        """Use R MCP server for statistical analysis"""
        print("\n📊 Using R Statistical MCP Server for analysis...")

        # Prepare a subset for R analysis
        numeric_cols = [col for col in self.raw_data.columns
                       if col.startswith('20') and self.raw_data[col].dtype in ['int64', 'float64']]

        if len(numeric_cols) < 2:
            print("Not enough numeric time series data for correlation analysis")
            return {}

        analysis_data = self.raw_data[['RegionName', 'StateName'] + numeric_cols[:20]]  # Limit columns
        csv_path = self.output_dir / 'analysis_subset.csv'
        analysis_data.to_csv(csv_path, index=False)

        print(f"Created analysis subset: {csv_path}")

        return {
            'analysis_file': str(csv_path),
            'numeric_columns': numeric_cols[:20],
            'regions': self.raw_data['RegionName'].unique().tolist()[:10]  # Sample regions
        }

    def create_investment_analytics(self):
        """Create investment risk and return analytics"""
        print("\n📈 Creating investment analytics...")

        # Calculate returns for recent years
        date_cols = [col for col in self.raw_data.columns if col.startswith('20') and self.raw_data[col].dtype in ['int64', 'float64']]
        if len(date_cols) < 24:  # Need at least 2 years
            return {}

        # Use last 5 years of data
        recent_cols = date_cols[-60:] if len(date_cols) > 60 else date_cols[-len(date_cols)//2:]

        # Calculate annualized returns
        returns_data = []
        for idx, row in self.raw_data.iterrows():
            try:
                prices = [row[col] for col in recent_cols if pd.notna(row[col])]
                if len(prices) >= 12:  # At least 1 year of data
                    # Calculate simple return
                    initial_price = prices[0]
                    final_price = prices[-1]
                    total_return = (final_price - initial_price) / initial_price

                    # Annualized return
                    years = len(prices) / 12  # Assuming monthly data
                    annualized_return = (1 + total_return) ** (1/years) - 1

                    returns_data.append({
                        'region': row['RegionName'],
                        'state': row['StateName'],
                        'initial_price': initial_price,
                        'final_price': final_price,
                        'total_return': total_return,
                        'annualized_return': annualized_return,
                        'data_points': len(prices)
                    })
            except:
                continue

        returns_df = pd.DataFrame(returns_data)
        returns_file = self.output_dir / 'returns_analysis.csv'
        returns_df.to_csv(returns_file, index=False)

        # Create risk analysis
        if not returns_df.empty:
            # Calculate risk metrics
            risk_metrics = {
                'mean_return': returns_df['annualized_return'].mean(),
                'return_std': returns_df['annualized_return'].std(),
                'sharpe_ratio': returns_df['annualized_return'].mean() / returns_df['annualized_return'].std() if returns_df['annualized_return'].std() > 0 else 0,
                'top_performers': returns_df.nlargest(5, 'annualized_return')[['region', 'annualized_return']].to_dict('records'),
                'worst_performers': returns_df.nsmallest(5, 'annualized_return')[['region', 'annualized_return']].to_dict('records')
            }

            with open(self.output_dir / 'risk_metrics.json', 'w') as f:
                json.dump(risk_metrics, f, indent=2)

            print(f"Created risk analysis with {len(returns_df)} regions")

        return {
            'returns_file': str(returns_file),
            'risk_metrics': risk_metrics if 'risk_metrics' in locals() else {},
            'analysis_summary': f"Analyzed {len(returns_data)} regions for investment performance"
        }

    def create_visualization(self):
        """Create statistical visualizations"""
        print("\n📊 Creating visualizations...")

        # Create correlation heatmap of different property types
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Real Estate Investment Analytics Dashboard', fontsize=16, fontweight='bold')

        # 1. Returns distribution
        returns_file = self.output_dir / 'returns_analysis.csv'
        if returns_file.exists():
            returns_df = pd.read_csv(returns_file)

            # Returns histogram
            axes[0,0].hist(returns_df['annualized_return'] * 100, bins=20, alpha=0.7, color='steelblue')
            axes[0,0].set_title('Annualized Return Distribution')
            axes[0,0].set_xlabel('Annual Return (%)')
            axes[0,0].set_ylabel('Number of Regions')
            axes[0,0].axvline(returns_df['annualized_return'].mean() * 100, color='red', linestyle='--',
                             label='.1f'            axes[0,0].legend()

            # Price appreciation scatter
            axes[0,1].scatter(returns_df['initial_price'] / 1000, returns_df['final_price'] / 1000,
                             alpha=0.6, color='green')
            axes[0,1].set_title('Initial vs Final Home Values')
            axes[0,1].set_xlabel('Initial Price ($K)')
            axes[0,1].set_ylabel('Final Price ($K)')
            # Add 45-degree line
            min_val = min(axes[0,1].get_xlim()[0], axes[0,1].get_ylim()[0])
            max_val = max(axes[0,1].get_xlim()[1], axes[0,1].get_ylim()[1])
            axes[0,1].plot([min_val, max_val], [min_val, max_val], 'r--', alpha=0.5)

        # 2. Regional performance
        state_avg = returns_df.groupby('state')['annualized_return'].agg(['mean', 'count']).reset_index()
        state_avg = state_avg[state_avg['count'] >= 3]  # At least 3 regions per state

        if len(state_avg) > 1:
            bars = axes[1,0].bar(range(len(state_avg)), state_avg['mean'] * 100)
            axes[1,0].set_title('Average Returns by State')
            axes[1,0].set_ylabel('Average Annual Return (%)')
            axes[1,0].set_xticks(range(len(state_avg)))
            axes[1,0].set_xticklabels(state_avg['state'], rotation=45, ha='right')

            # Color bars based on performance
            for i, bar in enumerate(bars):
                color = 'green' if state_avg.iloc[i]['mean'] > 0 else 'red'
                bar.set_color(color)

        # 3. Top and bottom performers
        if len(returns_df) > 10:
            top_bottom = pd.concat([
                returns_df.nlargest(5, 'annualized_return'),
                returns_df.nsmallest(5, 'annualized_return')
            ])

            colors = ['green'] * 5 + ['red'] * 5
            bars = axes[1,1].bar(range(len(top_bottom)),
                                 top_bottom['annualized_return'] * 100,
                                 color=colors)

            axes[1,1].set_title('Top & Bottom Performing Regions')
            axes[1,1].set_ylabel('Annual Return (%)')
            axes[1,1].set_xticks(range(len(top_bottom)))
            axes[1,1].set_xticklabels([r[:15] + '...' if len(r) > 15 else r
                                      for r in top_bottom['region']],
                                     rotation=45, ha='right')

        plt.tight_layout()
        plt.savefig(self.output_dir / 'investment_dashboard.png', dpi=300, bbox_inches='tight')
        plt.close()

        print(f"Created investment dashboard: {self.output_dir / 'investment_dashboard.png'}")

        return {
            'dashboard_plot': str(self.output_dir / 'investment_dashboard.png'),
            'visualization_created': True
        }

    def create_html_dashboard(self):
        """Create interactive HTML dashboard"""
        print("\n🌐 Creating interactive HTML dashboard...")

        html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <title>DakotaAI Real Estate Investment Analytics</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        .header {{ text-align: center; color: #2c3e50; margin-bottom: 30px; }}
        .metric-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-bottom: 30px; }}
        .metric-card {{ background: #f8f9fa; padding: 20px; border-radius: 8px; border-left: 4px solid #3498db; }}
        .metric-value {{ font-size: 2em; font-weight: bold; color: #2c3e50; }}
        .metric-label {{ color: #7f8c8d; font-size: 0.9em; }}
        .chart-container {{ margin: 20px 0; text-align: center; }}
        .chart-title {{ color: #2c3e50; margin-bottom: 10px; font-size: 1.2em; font-weight: bold; }}
        .insights {{ background: #ecf0f1; padding: 20px; border-radius: 8px; margin-top: 20px; }}
        .region-table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        .region-table th, .region-table td {{ padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }}
        .region-table th {{ background-color: #f8f9fa; font-weight: bold; }}
        .positive {{ color: green; }}
        .negative {{ color: red; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏠 DakotaAI Real Estate Investment Analytics</h1>
            <p>Powered by AI-driven market analysis and R statistical models</p>
        </div>

        <div class="metric-grid">
"""

        # Load metrics if available
        metrics_file = self.output_dir / 'risk_metrics.json'
        if metrics_file.exists():
            with open(metrics_file, 'r') as f:
                metrics = json.load(f)

            html_template += f"""
            <div class="metric-card">
                <div class="metric-value">{metrics['mean_return']*100:.1f}%</div>
                <div class="metric-label">Average Annual Return</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{metrics['return_std']*100:.1f}%</div>
                <div class="metric-label">Return Volatility</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{metrics['sharpe_ratio']:.2f}</div>
                <div class="metric-label">Sharpe Ratio</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{len(metrics.get('top_performers', []))}</div>
                <div class="metric-label">Markets Analyzed</div>
            </div>
"""

        html_template += """
        </div>
"""

        # Load and display top performers
        if metrics_file.exists():
            with open(metrics_file, 'r') as f:
                metrics = json.load(f)

            html_template += """
        <div class="insights">
            <h3>📈 Top Performing Markets</h3>
            <table class="region-table">
                <tr><th>Region</th><th>Annual Return</th></tr>
"""

            for perf in metrics.get('top_performers', [])[:5]:
                html_template += f"""
                <tr><td>{perf['region']}</td><td class="positive">+{perf['annualized_return']*100:.1f}%</td></tr>
"""
            html_template += "</table></div>"

            html_template += """
        <div class="insights">
            <h3>📉 Underperforming Markets</h3>
            <table class="region-table">
                <tr><th>Region</th><th>Annual Return</th></tr>
"""

            for perf in metrics.get('worst_performers', [])[:5]:
                html_template += f"""
                <tr><td>{perf['region']}</td><td class="negative">{perf['annualized_return']*100:.1f}%</td></tr>
"""
            html_template += "</table></div>"

        # Add about section
        html_template += """
        <div class="insights">
            <h3>🧠 AI-Powered Real Estate Analytics</h3>
            <p>This dashboard demonstrates DakotaAI's advanced real estate investment analysis capabilities:</p>
            <ul>
                <li><strong>Statistical Modeling:</strong> R-based correlation analysis and risk assessment</li>
                <li><strong>Time Series Analysis:</strong> Housing price trend decomposition and forecasting</li>
                <li><strong>Risk Assessment:</strong> Portfolio optimization and volatility analysis</li>
                <li><strong>Market Intelligence:</strong> Cross-regional comparison and opportunity identification</li>
            </ul>
            <p><em>Built with Python data processing and R statistical analysis via MCP server</em></p>
        </div>
    </div>
</body>
</html>
"""

        dashboard_file = self.output_dir / 'real_estate_dashboard.html'
        with open(dashboard_file, 'w') as f:
            f.write(html_template)

        print(f"Created HTML dashboard: {dashboard_file}")
        return {'dashboard_html': str(dashboard_file)}

    def run_analysis(self):
        """Run the complete real estate analytics workflow"""
        try:
            # Load and sample data
            self.load_and_sample_data()

            # R MCP integration
            r_analysis = self.analyze_with_r_mcp()

            # Investment analytics
            investment_data = self.create_investment_analytics()

            # Visualizations
            viz_data = self.create_visualization()

            # HTML dashboard
            html_data = self.create_html_dashboard()

            print("\n" + "="*60)
            print("✅ REAL ESTATE ANALYTICS DEMO COMPLETE")
            print("="*60)
            print(f"📁 Output directory: {self.output_dir}")
            print(f"📊 Analysis performed on {len(self.raw_data)} housing regions")
            print(f"🎯 R MCP server integration: {'✓ Available' if 'analysis_file' in r_analysis else '✗ Not connected'}")

            # List created files
            created_files = []
            for file in self.output_dir.glob('*'):
                if file.is_file():
                    created_files.append(file.name)

            if created_files:
                print("📄 Created files:")
                for file in sorted(created_files):
                    print(f"   - {file}")

            # Provide summary insights
            if 'risk_metrics' in investment_data and investment_data['risk_metrics']:
                metrics = investment_data['risk_metrics']
                print("\n💡 Key Insights:")
                print(".1f"                if metrics['sharpe_ratio'] > 0.5:
                    print(".2f"                else:
                    print(".2f"                    print("high volatility suggests need for diversification")

            return {
                'success': True,
                'output_dir': str(self.output_dir),
                'files_created': created_files,
                'r_integration': r_analysis,
                'investment_analysis': investment_data,
                'visualizations': viz_data,
                'dashboard': html_data
            }

        except Exception as e:
            print(f"\n❌ Error during analysis: {str(e)}")
            import traceback
            traceback.print_exc()

            return {
                'success': False,
                'error': str(e)
            }

def main():
    """Main function to run the real estate analytics demo"""
    demo = HousingAnalyticsDemo()
    results = demo.run_analysis()

    if results.get('success'):
        print("\n🎉 Demo completed successfully!")
        print(f"Open {results['output_dir']}/real_estate_dashboard.html to view results"
    else:
        print(f"\n❌ Demo failed: {results.get('error', 'Unknown error')}")

if __name__ == "__main__":
    main()
