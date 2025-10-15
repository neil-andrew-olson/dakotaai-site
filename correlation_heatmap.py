import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Set style for professional appearance
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

def load_and_clean_data(file_path):
    """Load and clean the sales data CSV file."""
    # Read the CSV file with error handling for inconsistent rows
    try:
        df = pd.read_csv(file_path, on_bad_lines='skip', engine='python')
    except:
        # Fallback: try reading with more permissive settings
        df = pd.read_csv(file_path, sep=',', header=0, error_bad_lines=False,
                        warn_bad_lines=False, quoting=3)

    print(f"Original dataset shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")

    # Handle case where column names might have issues
    if len(df.columns) > 7:
        # Keep only the first 7 columns (OrderDate, Region, Product, Sales, Quantity, Discount, MissingCol)
        df = df.iloc[:, :7]
        df.columns = ['OrderDate', 'Region', 'Product', 'Sales', 'Quantity', 'Discount', 'MissingCol']

    # Clean column names and data
    df.columns = df.columns.str.strip()

    # Convert numeric columns, handling missing values and invalid entries
    numeric_cols = ['Sales', 'Quantity', 'Discount']

    for col in numeric_cols:
        # Convert to numeric, forcing errors to NaN
        df[col] = pd.to_numeric(df[col], errors='coerce')

        # Remove unreasonable values (negative sales, extreme outliers)
        if col == 'Sales':
            df[col] = df[col].where((df[col] >= 0) & (df[col] <= 50000), np.nan)
        elif col == 'Quantity':
            df[col] = df[col].where((df[col] >= 0) & (df[col] <= 1000), np.nan)
        elif col == 'Discount':
            df[col] = df[col].where((df[col] >= 0) & (df[col] <= 1), np.nan)

    # Remove rows where all numeric values are missing
    df_clean = df.dropna(how='all', subset=numeric_cols)

    print(f"Cleaned dataset shape: {df_clean.shape}")
    print(f"Missing values per column:\n{df_clean[numeric_cols].isnull().sum()}")

    return df_clean[numeric_cols]

def calculate_correlations_and_significance(data):
    """Calculate correlation matrix and statistical significance."""
    # Drop rows with any NaN values for correlation analysis
    data_clean = data.dropna()

    # Calculate correlation matrix
    corr_matrix = data_clean.corr(method='pearson')

    # Calculate p-values for each correlation pair
    p_values = pd.DataFrame(np.nan, index=corr_matrix.index, columns=corr_matrix.columns)

    n = len(data_clean)
    for i in range(len(corr_matrix.columns)):
        for j in range(i+1, len(corr_matrix.columns)):
            col1, col2 = corr_matrix.columns[i], corr_matrix.columns[j]
            corr_val = corr_matrix.loc[col1, col2]

            # Fisher's r-to-z transformation
            z = 0.5 * np.log((1 + corr_val) / (1 - corr_val + 1e-10))
            se = 1 / np.sqrt(n - 3)
            z_score = z / se

            # Two-tailed test
            p_val = 2 * (1 - stats.norm.cdf(abs(z_score)))
            p_values.loc[col1, col2] = p_val
            p_values.loc[col2, col1] = p_val

    return corr_matrix, p_values

def create_correlation_heatmap(corr_matrix, p_values, data):
    """Create and save a professional correlation heatmap with significance markers."""
    # Set up the figure with custom size for high resolution
    fig, ax = plt.subplots(figsize=(10, 8), dpi=300)

    # Create mask for upper triangle
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

    # Create the heatmap
    cmap = sns.diverging_palette(220, 20, as_cmap=True)

    # Plot heatmap
    sns.heatmap(corr_matrix, mask=mask, cmap=cmap, vmax=1, vmin=-1, center=0,
                square=True, linewidths=0.5, annot=True, fmt='.3f', cbar_kws={'shrink': 0.8},
                ax=ax)

    # Add significance markers
    for i in range(len(corr_matrix.columns)):
        for j in range(i+1, len(corr_matrix.columns)):
            col1, col2 = corr_matrix.columns[i], corr_matrix.columns[j]
            p_val = p_values.loc[col1, col2]

            # Position for the significance marker
            x_pos = j + 0.5
            y_pos = i + 0.5

            # Add significance stars
            if p_val < 0.001:
                marker = '***'
            elif p_val < 0.01:
                marker = '**'
            elif p_val < 0.05:
                marker = '*'
            else:
                marker = 'ns'  # not significant

            # Add text annotation for significance
            ax.text(x_pos, y_pos, marker, ha='center', va='center',
                   fontsize=14, fontweight='bold', color='white',
                   bbox=dict(boxstyle="round,pad=0.2", facecolor='black', alpha=0.8))

    # Customize the plot
    ax.set_title('Sales Data Correlation Heatmap\n(Statistical Significance: *p<0.05, **p<0.01, ***p<0.001)',
                fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('')
    ax.set_ylabel('')

    # Add sample size annotation
    data_clean = data.dropna()
    ax.text(0.02, 0.98, f'n = {len(data_clean)} observations',
            transform=ax.transAxes, fontsize=12, verticalalignment='top',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

    # Adjust layout
    plt.tight_layout()

    # Save as high-resolution PNG
    plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print("High-resolution correlation heatmap saved as 'correlation_heatmap.png'")

    # Show plot
    plt.show()

def generate_summary_statistics(data):
    """Generate summary statistics for the numeric variables."""
    print("\n" + "="*60)
    print("SUMMARY STATISTICS")
    print("="*60)

    numeric_cols = ['Sales', 'Quantity', 'Discount']

    for col in numeric_cols:
        col_data = data[col].dropna()
        print(f"\n{col}:")
        print(f"  Mean: {col_data.mean():.2f}")
        print(f"  Median: {col_data.median():.2f}")
        print(f"  Std Dev: {col_data.std():.2f}")
        print(f"  Min: {col_data.min():.2f}")
        print(f"  Max: {col_data.max():.2f}")
        print(f"  Valid observations: {len(col_data)}")
        print(f"  Missing values: {data[col].isnull().sum()}")

def main():
    """Main function to execute the correlation heatmap analysis."""
    file_path = 'demos/sales_data.csv'

    try:
        # Load and clean data
        print("Loading and cleaning data...")
        data = load_and_clean_data(file_path)

        if data.empty or len(data.dropna()) < 3:
            print("Insufficient data for correlation analysis.")
            return

        # Generate summary statistics
        generate_summary_statistics(data)

        # Calculate correlations and significance
        print("\nCalculating correlations and statistical significance...")
        corr_matrix, p_values = calculate_correlations_and_significance(data)

        # Display correlation matrix
        print("\n" + "="*60)
        print("CORRELATION MATRIX")
        print("="*60)
        print(corr_matrix.round(4))

        # Display p-values
        print("\n" + "="*60)
        print("P-VALUES MATRIX")
        print("="*60)
        print(p_values.round(4))

        # Create and save heatmap
        print("\nCreating correlation heatmap...")
        create_correlation_heatmap(corr_matrix, p_values, data)

        print("\n" + "="*60)
        print("ANALYSIS COMPLETE")
        print("="*60)
        print("✓ Correlation heatmap created successfully")
        print("✓ Statistical significance markers added")
        print("✓ High-resolution PNG saved")

    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        print("Please check the data format and try again.")

if __name__ == "__main__":
    main()
