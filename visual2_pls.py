import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
from matplotlib import rcParams
import webbrowser
def set_rcParams():
    rcParams['xtick.labelsize']=12
    rcParams['ytick.labelsize']=12
    rcParams['figure.figsize']=18,8
def load_data(file_path):
    return pd.read_csv(file_path)
def plot_data(df, pdf_path):
    height_box=df['x1']
    weight_box=df['Target']
    team_box=df['abc']
    fig_1,p=plt.subplots(figsize=(7,4))
    p=sns.scatterplot(x=height_box, y=weight_box, style=team_box, hue=team_box, palette=['red','green','blue'])
    sns.set_style('whitegrid', {'grid.linestyle':'--'})
    p.set_xlabel('x1',fontsize=16)
    p.set_ylabel('Target',fontsize=16)
    p.legend(loc=2,bbox_to_anchor=(1,1))
    fig_1.subplots_adjust(left=0.13, right=0.8, bottom=0.16, top=0.93)
    fig_1.savefig(pdf_path, facecolor='white')
    plt.show()
    plt.close()
def open_pdf(pdf_path):
    webbrowser.open_new(pdf_path)
def main():
    set_rcParams()
    base_folder=r'C:\\Users\\user\\git\\github\\py2312_visual_pls\\'
    file_name=base_folder+'regression_pls.csv'
    pdf_name=base_folder+'pdf\\visual2_pls.pdf'
    df=load_data(file_name)
    plot_data(df, pdf_name)
    open_pdf(pdf_name)
if __name__=="__main__":
    main()