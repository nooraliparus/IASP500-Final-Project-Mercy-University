"""
Threat Taxonomy Builder for AI-Powered Cyber Attacks
Author: IASP500 Team
Date: Fall 2025
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class ThreatTaxonomy:
    def __init__(self):
        self.categories = {
            'social_engineering': [],
            'malware_generation': [],
            'vulnerability_discovery': [],
            'defense_evasion': [],
            'automated_attacks': []
        }
    
    def add_threat(self, category, threat_name, techniques, tools, efficacy):
        """Add a threat to the taxonomy"""
        threat = {
            'name': threat_name,
            'techniques': techniques,
            'tools': tools,
            'efficacy': efficacy  # Scale 1-10
        }
        self.categories[category].append(threat)
    
    def generate_visualization(self):
        """Generate bar chart of threat efficacy by category"""
        category_avg = {}
        for category, threats in self.categories.items():
            if threats:
                avg_efficacy = sum(t['efficacy'] for t in threats) / len(threats)
                category_avg[category] = avg_efficacy
        
        # Create visualization
        plt.figure(figsize=(10, 6))
        categories = list(category_avg.keys())
        values = list(category_avg.values())
        
        bars = plt.bar(categories, values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
        plt.title('Average Threat Efficacy by Category', fontsize=14)
        plt.xlabel('Threat Category', fontsize=12)
        plt.ylabel('Average Efficacy (1-10 scale)', fontsize=12)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{height:.1f}', ha='center', va='bottom')
        
        plt.tight_layout()
        plt.savefig('threat_efficacy_analysis.png', dpi=300)
        plt.show()
        
        return category_avg
    
    def export_to_csv(self, filename='threat_taxonomy.csv'):
        """Export taxonomy data to CSV"""
        data = []
        for category, threats in self.categories.items():
            for threat in threats:
                data.append({
                    'Category': category.replace('_', ' ').title(),
                    'Threat Name': threat['name'],
                    'Techniques': ', '.join(threat['techniques']),
                    'Tools': ', '.join(threat['tools']),
                    'Efficacy': threat['efficacy']
                })
        
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        return df

# Example usage
if __name__ == "__main__":
    taxonomy = ThreatTaxonomy()
    
    # Add example threats (from research)
    taxonomy.add_threat(
        category='social_engineering',
        threat_name='AI-Generated Phishing',
        techniques=['LLM-based email generation', 'Context-aware personalization'],
        tools=['GPT-4', 'WormGPT', 'FraudGPT'],
        efficacy=8.5
    )
    
    taxonomy.add_threat(
        category='malware_generation',
        threat_name='GAN-based Polymorphic Malware',
        techniques=['Adversarial sample generation', 'Signature evasion'],
        tools=['MalGAN', 'GAN-based malware generators'],
        efficacy=7.2
    )
    
    # Generate analysis
    results = taxonomy.generate_visualization()
    print("Threat Efficacy Analysis:", results)
    
    # Export data
    df = taxonomy.export_to_csv()
    print("\nTaxonomy exported to CSV:")
    print(df.head())