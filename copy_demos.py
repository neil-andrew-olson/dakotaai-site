#!/usr/bin/env python3
"""
Script to copy all demo files from demos/ to dakotaai-demos/apps/ structure
"""

import os
import shutil

def copy_demo_files():
    print("📁 Copying demo files to monorepo structure...")

    # Source and destination paths
    source_dir = "demos"
    dest_dir = "dakotaai-demos/apps"

    if not os.path.exists(source_dir):
        print(f"❌ Source directory '{source_dir}' not found!")
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"✅ Created destination directory: {dest_dir}")

    # Demo mapping - file -> app name
    demo_mapping = {
        'crypto.html': 'crypto-analyzer',
        'dataset.html': 'titanic-analyzer',
        'fake_news.html': 'fake-news-detector',
        'iris.html': 'iris-classifier',
        'heart_disease.html': 'heart-disease-predictor',
        'bitcoin.html': 'bitcoin-forecaster',
        'sales.html': 'sales-analyzer',
        'iris_demo.py': 'iris-classifier',
        'heart_disease.py': 'heart-disease-predictor',
        'fake_news.py': 'fake-news-detector',
        'bitcoin.py': 'bitcoin-forecaster'
    }

    # Data files to copy
    data_files = [
        'titanic.csv',
        'sample_stock.csv',
        'sales_data.csv'
    ]

    files_copied = []

    # Copy HTML and Python files
    for filename, app_name in demo_mapping.items():
        src_file = os.path.join(source_dir, filename)
        if os.path.exists(src_file):
            # Create app directory
            app_dir = os.path.join(dest_dir, app_name)
            if not os.path.exists(app_dir):
                os.makedirs(app_dir)

            # Copy file
            dest_file = os.path.join(app_dir, filename)
            shutil.copy2(src_file, dest_file)
            files_copied.append(dest_file)
            print(f"✅ Copied: {filename} -> apps/{app_name}/")

    # Copy data files to appropriate apps
    data_mapping = {
        'titanic.csv': 'titanic-analyzer',
        'sample_stock.csv': 'crypto-analyzer',
        'sales_data.csv': 'sales-analyzer'
    }

    for data_file, app_name in data_mapping.items():
        src_file = os.path.join(source_dir, data_file)
        if os.path.exists(src_file):
            app_dir = os.path.join(dest_dir, app_name)
            if not os.path.exists(app_dir):
                os.makedirs(app_dir)

            dest_file = os.path.join(app_dir, data_file)
            shutil.copy2(src_file, dest_file)
            files_copied.append(dest_file)
            print(f"✅ Copied data: {data_file} -> apps/{app_name}/")

    print(f"\n🎉 Successfully copied {len(files_copied)} files!")
    print("\n📁 Repository structure ready for git push!")

    return files_copied

if __name__ == "__main__":
    copy_demo_files()
