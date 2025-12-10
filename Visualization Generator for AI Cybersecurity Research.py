"""
Visualization Generator for AI Cybersecurity Research
Author: IASP500 Team
Date: Fall 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Set professional styling
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
rcParams['axes.grid'] = True
rcParams['grid.alpha'] = 0.3

def create_comparative_bar_chart():
    """Create Figure 2: Comparative Efficacy of AI vs Traditional Attacks"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    categories = ['AI-Generated Phishing', 'Human-Crafted Phishing', 'Generic Phishing']
    success_rates = [68, 45, 23]
    colors = ['#2E86AB', '#A23B72', '#F18F01']
    
    bars = ax.bar(categories, success_rates, color=colors, width=0.6)
    ax.set_ylabel('Success Rate (%)', fontsize=12, fontweight='bold')
    ax.set_title('Comparative Efficacy of AI vs. Traditional Social Engineering Attacks', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Add value labels
    for bar, rate in zip(bars, success_rates):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{rate}%', ha='center', va='bottom', fontweight='bold')
    
    # Add data source
    ax.text(0.02, -0.15, 'Source: Wang et al., 2024; Verizon DBIR 2023', 
            transform=ax.transAxes, fontsize=9, style='italic')
    
    plt.tight_layout()
    plt.savefig('figure2_comparative_efficacy.png', dpi=300, bbox_inches='tight')
    plt.show()
    return fig

def create_detection_time_chart():
    """Create Figure 3: Reduction in Detection Times"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # MTTD Subplot
    mttd_labels = ['Traditional SIEM', 'AI-Augmented SIEM']
    mttd_values = [21.0, 3.2]
    colors_mttd = ['#E63946', '#457B9D']
    
    bars1 = ax1.bar(mttd_labels, mttd_values, color=colors_mttd, width=0.5)
    ax1.set_ylabel('Mean Time to Detect (Days)', fontweight='bold')
    ax1.set_title('MTTD Comparison', fontweight='bold')
    
    for bar, val in zip(bars1, mttd_values):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{val} days', ha='center', va='bottom', fontweight='bold')
    
    # MTTR Subplot
    mttr_labels = ['Manual Processes', 'SOAR + AI']
    mttr_values = [18.5, 4.6]
    colors_mttr = ['#E9C46A', '#2A9D8F']
    
    bars2 = ax2.bar(mttr_labels, mttr_values, color=colors_mttr, width=0.5)
    ax2.set_ylabel('Mean Time to Respond (Hours)', fontweight='bold')
    ax2.set_title('MTTR Comparison', fontweight='bold')
    
    for bar, val in zip(bars2, mttr_values):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.3,
                f'{val} hours', ha='center', va='bottom', fontweight='bold')
    
    fig.suptitle('Reduction in Detection and Response Times with AI-Enhanced Security Operations', 
                 fontsize=14, fontweight='bold', y=1.02)
    
    # Add data source
    fig.text(0.02, 0.02, 'Source: Exabeam 2023 Report; Palo Alto Networks Case Studies', 
             fontsize=9, style='italic')
    
    plt.tight_layout()
    plt.savefig('figure3_detection_times.png', dpi=300, bbox_inches='tight')
    plt.show()
    return fig

def create_adversarial_success_chart():
    """Create Figure 4: Success Rates of Adversarial Attacks"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    attack_types = ['Evasion Attacks\n(Image/Content Filters)', 
                    'Poisoning Attacks\n(Training Data)', 
                    'Model Extraction Attacks']
    success_rates = [82, 73, 61]
    
    # Create gradient colors
    colors = plt.cm.RdYlGn_r(np.array(success_rates)/100)
    
    bars = ax.bar(attack_types, success_rates, color=colors, width=0.6, edgecolor='black')
    ax.set_ylabel('Success Rate (%)', fontsize=12, fontweight='bold')
    ax.set_title('Success Rates of Adversarial Attacks Against ML Defenses\n(Without Proper Hardening)', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_ylim(0, 100)
    
    # Add value labels and horizontal lines
    for bar, rate in zip(bars, success_rates):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 2,
                f'{rate}%', ha='center', va='bottom', fontweight='bold')
        ax.axhline(y=rate, xmin=bar.get_x()/len(attack_types), 
                  xmax=(bar.get_x() + bar.get_width())/len(attack_types),
                  color='gray', linestyle='--', alpha=0.5)
    
    # Add risk level annotations
    risk_levels = ['High Risk', 'High Risk', 'Medium Risk']
    for i, (bar, level) in enumerate(zip(bars, risk_levels)):
        ax.text(bar.get_x() + bar.get_width()/2., -8,
                level, ha='center', va='top', fontsize=10,
                bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgray', alpha=0.7))
    
    ax.text(0.02, -0.15, 'Source: Apruzzese et al., IEEE TNNLS 2022', 
            transform=ax.transAxes, fontsize=9, style='italic')
    
    plt.tight_layout()
    plt.savefig('figure4_adversarial_success.png', dpi=300, bbox_inches='tight')
    plt.show()
    return fig

def create_swot_analysis_diagram():
    """Create SWOT Analysis Visualization"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    
    # Strengths of Offensive AI
    strengths_data = {
        'Lower skill barrier': 9.0,
        'Attack automation': 8.5,
        'Scalable personalization': 8.2,
        'Adversarial bypass': 7.8
    }
    
    ax1.barh(list(strengths_data.keys()), list(strengths_data.values()), color='#2E8B57')
    ax1.set_title('Strengths of Offensive AI', fontweight='bold')
    ax1.set_xlim(0, 10)
    
    # Weaknesses of Offensive AI
    weaknesses_data = {
        'Human guidance needed': 6.5,
        'Limited adaptability': 7.2,
        'Detectable artifacts': 6.8,
        'High compute costs': 7.0
    }
    
    ax2.barh(list(weaknesses_data.keys()), list(weaknesses_data.values()), color='#DC143C')
    ax2.set_title('Weaknesses of Offensive AI', fontweight='bold')
    ax2.set_xlim(0, 10)
    
    # Strengths of Defensive AI
    defense_strengths = {
        'Massive data processing': 9.5,
        'Anomaly detection': 9.0,
        'Continuous adaptation': 8.7,
        'Task automation': 8.5
    }
    
    ax3.barh(list(defense_strengths.keys()), list(defense_strengths.values()), color='#1E90FF')
    ax3.set_title('Strengths of Defensive AI', fontweight='bold')
    ax3.set_xlim(0, 10)
    
    # Weaknesses of Defensive AI
    defense_weaknesses = {
        'Adversarial vulnerability': 8.0,
        'False positive rates': 7.5,
        'Training data needs': 7.8,
        'Black box interpretability': 7.2
    }
    
    ax4.barh(list(defense_weaknesses.keys()), list(defense_weaknesses.values()), color='#FF8C00')
    ax4.set_title('Weaknesses of Defensive AI', fontweight='bold')
    ax4.set_xlim(0, 10)
    
    fig.suptitle('SWOT Analysis: AI in Cybersecurity (Weighted Assessment 1-10)', 
                 fontsize=16, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    plt.savefig('swot_analysis_diagram.png', dpi=300, bbox_inches='tight')
    plt.show()
    return fig

if __name__ == "__main__":
    print("Generating research visualizations...")
    
    # Generate all figures
    fig1 = create_comparative_bar_chart()
    fig2 = create_detection_time_chart()
    fig3 = create_adversarial_success_chart()
    fig4 = create_swot_analysis_diagram()
    
    print("All visualizations generated successfully!")
    print("Files created:")
    print("- figure2_comparative_efficacy.png")
    print("- figure3_detection_times.png")
    print("- figure4_adversarial_success.png")
    print("- swot_analysis_diagram.png")