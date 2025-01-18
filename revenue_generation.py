import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


plt.style.use('seaborn')
sns.set_palette("husl")

# Create the dataset
data = {
    'Product': ['Budweiser Can (Pack of 6)', 'Budweiser Bottle (Pack of 6)', 'Budweiser Can (Pack of 12)',
                'Stella Artois Can (Pack of 6)', 'Stella Artois Bottle (Pack of 6)', 'Stella Artois Can (Pack of 12)',
                'Competitor Can (Pack of 6)', 'Competitor Bottle (Pack of 6)', 'Competitor Can (Pack of 12)'],
    'Store_A': [20, 6, 8, 123, 108, 78, 68, 37, 12],
    'Store_B': [65, 35, 24, 163, 105, 28, 274, 143, 53],
    'Store_C': [163, 82, 74, 32, 10, 5, 11, 8, 8],
    'Price': [750, 800, 1400, 900, 950, 1700, 650, 700, 1200]
}

df = pd.DataFrame(data)


for store in ['Store_A', 'Store_B', 'Store_C']:
    df[f'{store}_Revenue'] = df[store] * df['Price']

def create_brand_revenue_comparison():
    """Creates a stacked bar chart comparing revenue by brand across stores"""
    plt.figure(figsize=(12, 6))
    

    brands = ['Budweiser', 'Stella Artois', 'Competitor']
    store_revenues = []
    
    for store in ['Store_A', 'Store_B', 'Store_C']:
        brand_rev = []
        for brand in brands:
            revenue = df[df['Product'].str.contains(brand)][f'{store}_Revenue'].sum()
            brand_rev.append(revenue)
        store_revenues.append(brand_rev)
    
    store_revenues = np.array(store_revenues)
    
  
    bar_width = 0.35
    r = np.arange(len(['Store A', 'Store B', 'Store C']))
    
    plt.bar(r, store_revenues[:, 0], width=bar_width, label='Budweiser')
    plt.bar(r, store_revenues[:, 1], width=bar_width, bottom=store_revenues[:, 0], label='Stella Artois')
    plt.bar(r, store_revenues[:, 2], width=bar_width, bottom=store_revenues[:, 0] + store_revenues[:, 1], label='Competitor')
    
    plt.title('Revenue Distribution by Brand and Store', fontsize=14, pad=20)
    plt.xlabel('Store', fontsize=12)
    plt.ylabel('Revenue (₹)', fontsize=12)
    plt.xticks(r, ['Store A', 'Store B', 'Store C'])
    plt.legend()
    
    return plt

def create_package_performance():
    """Creates a grouped bar chart showing performance by package type"""
    plt.figure(figsize=(12, 6))
    

    package_types = ['Can (Pack of 6)', 'Bottle (Pack of 6)', 'Can (Pack of 12)']
    revenues = []
    
    for pkg in package_types:
        rev = df[df['Product'].str.contains(pkg)]['Store_A_Revenue'].sum() + \
              df[df['Product'].str.contains(pkg)]['Store_B_Revenue'].sum() + \
              df[df['Product'].str.contains(pkg)]['Store_C_Revenue'].sum()
        revenues.append(rev)
    
    plt.bar(package_types, revenues)
    plt.title('Revenue by Package Type', fontsize=14, pad=20)
    plt.xlabel('Package Type', fontsize=12)
    plt.ylabel('Total Revenue (₹)', fontsize=12)
    plt.xticks(rotation=45)
    
  
    for i, v in enumerate(revenues):
        plt.text(i, v, f'₹{int(v):,}', ha='center', va='bottom')
    
    return plt

def create_price_volume_analysis():
    """Creates a scatter plot with price vs volume relationship"""
    plt.figure(figsize=(10, 6))
    

    df['Total_Units'] = df['Store_A'] + df['Store_B'] + df['Store_C']
    
 
    plt.scatter(df['Price'], df['Total_Units'], 
               s=df['Total_Units']*2,
               alpha=0.6)
    

    z = np.polyfit(df['Price'], df['Total_Units'], 1)
    p = np.poly1d(z)
    plt.plot(df['Price'], p(df['Price']), "r--", alpha=0.8)
    
    plt.title('Price vs Volume Analysis', fontsize=14, pad=20)
    plt.xlabel('Price (₹)', fontsize=12)
    plt.ylabel('Total Units Sold', fontsize=12)
   
    for i, txt in enumerate(df['Product']):
        plt.annotate(txt.split('(')[0], 
                    (df['Price'].iloc[i], df['Total_Units'].iloc[i]),
                    xytext=(5, 5), textcoords='offset points',
                    fontsize=8)
    
    return plt

def create_store_heatmap():
    """Creates a heatmap showing performance across stores"""
    plt.figure(figsize=(12, 8))
    
   
    heatmap_data = df.pivot_table(
        values=['Store_A_Revenue', 'Store_B_Revenue', 'Store_C_Revenue'],
        index='Product',
        aggfunc='sum'
    )
    

    sns.heatmap(heatmap_data, 
                annot=True, 
                fmt=',d',
                cmap='YlOrRd',
                cbar_kws={'label': 'Revenue (₹)'})
    
    plt.title('Revenue Heatmap by Product and Store', fontsize=14, pad=20)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    
    return plt


def save_all_visualizations():
    """Saves all visualizations to files"""
    
 
    create_brand_revenue_comparison()
    plt.savefig('brand_revenue_comparison.png', bbox_inches='tight', dpi=300)
    plt.close()
    
 
    create_package_performance()
    plt.savefig('package_performance.png', bbox_inches='tight', dpi=300)
    plt.close()
    
   
    create_price_volume_analysis()
    plt.savefig('price_volume_analysis.png', bbox_inches='tight', dpi=300)
    plt.close()
    
  
    create_store_heatmap()
    plt.savefig('store_heatmap.png', bbox_inches='tight', dpi=300)
    plt.close()


save_all_visualizations()