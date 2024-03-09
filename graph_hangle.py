import matplotlib as mpl
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

def main():
    path = '/System/Library/Fonts/AppleSDGothicNeo.ttc'
    font_name = fm.FontProperties(fname = path, size = 50).get_name()
    plt.rc('font', family = font_name)
    mpl.rcParams['axes.unicode_minus'] = False

if __name__ == "__main__":
    main()