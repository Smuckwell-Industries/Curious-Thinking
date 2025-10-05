"""
HBR-style Matplotlib plot styling for consistent diagram aesthetics.
"""
import matplotlib.pyplot as plt
import matplotlib as mpl

# Standard figure sizes for consistency across visualizations
STANDARD_FIGURE_SIZES = {
    'square_small': (7.5, 7.5),
    'square_medium': (10, 10),
    'square_large': (12, 12),
    'wide': (12, 8),
    'tall': (8, 12)
}

def apply_hbr_style():
    """Apply HBR-style settings to the current matplotlib plot."""
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']
    plt.rcParams['axes.labelsize'] = 11
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10

# Color palette
HBR_COLORS = {
    # Core colors
    'blue': "#084B8A",           # Dark blue for headers and main elements
    'light_blue': "#E6F1F5",     # Light blue for backgrounds
    'accent_blue': "#2E86C1",    # Medium blue for accents and arrows
    'text': "#333333",           # Dark gray for main text
    'light_text': "#555555",     # Light gray for secondary text
    
    # Quadrant colors - lighter, professional tones
    'quadrant1': '#e6f2e6',      # Light green
    'quadrant2': '#e6f0f7',      # Light blue
    'quadrant3': '#f2f2e6',      # Light yellow
    'quadrant4': '#f7e6e6',      # Light red
    
    # Background
    'background': "#F8F9FA",     # Very light gray for backgrounds
    'white': "#FFFFFF"           # White
}

# Text box styles
def clean_text_box(color=None):
    """Return a clean text box style."""
    if color is None:
        color = HBR_COLORS['blue']
    
    return dict(
        facecolor='white', 
        edgecolor=color, 
        alpha=0.9, 
        boxstyle="round,pad=0.4", 
        linewidth=0.5
    )

def set_figure_aesthetics(fig, ax, title=None, subtitle=None):
    """
    Set common figure aesthetics including title and subtitle.
    
    Parameters:
    - fig: matplotlib figure
    - ax: matplotlib axis
    - title: main title text (optional)
    - subtitle: subtitle text (optional)
    """
    # Remove spines for cleaner look
    for spine in ['top', 'right', 'bottom', 'left']:
        ax.spines[spine].set_visible(False)
    
    # Turn off grid
    plt.grid(False)
    
    # Set background color
    fig.set_facecolor(HBR_COLORS['white'])
    
    # Add title and subtitle if provided
    if title:
        fig.suptitle(title, fontsize=16, fontweight='bold', 
                    y=0.98, color=HBR_COLORS['text'])
        
        if subtitle:
            plt.figtext(0.5, 0.94, subtitle, fontsize=11, ha='center',
                      style='italic', color=HBR_COLORS['light_text'])
            plt.tight_layout(rect=[0, 0, 1, 0.92])  # Adjust for both title and subtitle
        else:
            plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust for title only
    else:
        plt.tight_layout()