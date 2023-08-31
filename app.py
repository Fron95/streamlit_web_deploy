import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import pandas as pd
import numpy as np

# 페이지 설정
# plot properties
    
# props = {
#         "alpha" : None,             # float or None (default: None)
#         "animated" : False,         # bool (default: False)
#         "antialiased" : True,       # bool (default: True)
#         "clip_box" : None,          # `~.bbox.Bbox` or tuple of float (default: None)
#         "clip_on" : True,           # bool (default: True)
#         "clip_path" : None,         # `~matplotlib.path.Path` or `~.transforms.Transform` or None (default: None)
#         "color" : None,             # color (default: 'C0')
#         "dash_capstyle" : 'butt',   # 'butt', 'round', 'projecting' (default: 'butt')
#         "dash_joinstyle" : 'round', # 'miter', 'round', 'bevel' (default: 'round')
#         "dashes" : None,            # sequence of floats (default: None)
#         "data" : None,              # (2, N) array_like or list (default: None)
#         "drawstyle" : None,         # 'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post' or None (default: None)
#         "figure" : None,            # `~matplotlib.figure.Figure` or int or str or None (default: None)
#         "fillstyle" : 'full',       # 'full', 'left', 'right', 'bottom', 'top', 'none' (default: 'full')
#         "label" : data.columns,
#         "gid" : None,               # str or None (default: None)
#         "linestyle" : '-',          # '-' or '--' or '-.' or ':' or 'None' or ' ' or '' or (offset, on-off-seq) or `~.collections.LineCollection` (default: '-')
#         "linewidth" : None,         # float or None (default: None)
#         "marker" : None,            # str or `~.markers.MarkerStyle` (default: 'None')
#         "markeredgecolor" : None,   # color or 'none' or None (default: 'auto')
#         "markeredgewidth" : None,   # float or None (default: `~.rcParams['lines.markeredgewidth']` = 1.0)
#         "markerfacecolor" : None,   # color or 'none' or None (default: 'auto')
#         "markerfacecoloralt" : 'none', # color or 'none' or None (default: 'none')
#         "markersize" : None,        # float or None (default: `~.rcParams['lines.markersize']` ** 2 = 36.0)
#         "markevery" : None,         # None or int or (int, int) or slice or list[int] or float or (float, float) or list[bool] (default: None)
#         "path_effects" : None      # `~.path_effects.AbstractPathEffect` or None (default: None)
# }



# 필용한 사전 정의

# def plot_graph(ax, x, y, title, color, linewidth, show_legend, label):
#     ax.plot(x, y, color=color, linewidth=linewidth, label=label)
#     ax.set_xlabel('X Axis')
#     ax.set_ylabel('Y Axis')
#     ax.set_title(title)
#     if show_legend:
#         ax.legend()
# 
# def name_generator(start_num=1) :
# 
# 
#     while True :
#         name = "label_{}".format(start_num)
#         start_num += 1
#         
# 
#         yield name    

# name_gen = name_generator()



# STREAMLIT 연동.
# STREAMLIT 연동.
# STREAMLIT 연동.
# STREAMLIT 연동.



def rgba2hex(rgba):

    color_hex = "#{0:02x}{1:02x}{2:02x}".format(int(rgba[0]*255), int(rgba[1]*255), int(rgba[2]*255))
    return color_hex




def main():
    

   

    st.set_page_config(layout="wide")

    # 제목설정
    st.title("Here is Your Plot !!")    
    st.markdown(f"해당 웹서비스는 더 편리한 데이터시각화를 가능하게 합니다. \n 계량적 분석 결과를 더욱 직관적으로 알 수 있또록 하는 데이터시각화의 기능이 매우 중요하다고 생각하여, \
    코딩에 능하지 않은 일반 사용자도  강력한 시각화 라이브러리인 matplotlib을 활용할 수 있도록 할 목적에서 개발되었습니다.")
                



    # 사이드바(1) - csv 파일 업로드
    data_uploading = st.sidebar.file_uploader("#### STEP1 : CSV 파일 업로드", type="csv")
    with open("10stocks.csv") as sample :
        sample_download = st.sidebar.download_button("샘플csv파일 다운로드하기", data=sample, file_name="sample_csv.csv")
    st.sidebar. write("** 데이터는 csv 포맷만 업로드 가능합니다. (excel은 추후 개발예정)")      
    data_info = st.sidebar.markdown("# 꼭 체크해주세요! 데이터 형태파악") 
    # st.sidebar.write("<p style='font-size: 40px;'>This is a paragraph with font size 16px</p>", unsafe_allow_html=True)

     # initial figure
    if data_uploading is None :        
        x = np.linspace(0, 2*np.pi, 100)
        y_sin = np.sin(x)
        df = pd.DataFrame({
        "sin" : y_sin,
        "cos" : -y_sin
        })

        fig, ax = plt.subplots()
        ax.plot(df)
        plt.fill_between(df.index, y1=df["sin"], alpha=0.7)                
        plt.fill_between(df.index, y1=df["cos"], alpha=0.7)
        st.write(fig)


    
    elif data_uploading is not None :
        # index 포함여부 확인
        index_included = st.sidebar.checkbox("first column is index", True)
        index_datetime = st.sidebar.checkbox("Index is Datetime type", True)
        column_name_included = st.sidebar.checkbox("first row is column name", True)
        # 판다스 데이터프레임으로 제작
        df = pd.read_csv(data_uploading, 
                         header=0 if column_name_included==1 else None)
        
        df.set_index(df.columns[0], inplace=True) if index_included==1 else ""
        if index_datetime is True :
             df.index = pd.to_datetime(df.index)
        
        # 그려지는 그래프 갯수 확인
        num_graphs = len(df.columns)
        labels = df.columns

                # 본문(3) - 표 출력
        
        #st.write("개선사항")
        #st.write(f"1. 칼라맵 색상표 제공 \n\
        #         8. index str  // float(int) // timestep인 경우에 따라 문제없이 들어갈 수 있게 제공 = type으로 자동인식하게하기.\
        #        * 특히 timestep 인 경우에는 format 수정방법 제공,\
        #        9. plt.subplots 기능 제공하기.\
        #        13. 기능별로 expander 정리하기.\
        #        14. 박스 / 화살표 표시하기 (annotation)\
        #        15. 경계표시하기 (plt.axhline,plt.axvline\
        #        16. 말상자넣기\
        #        17. 예시 템플릿 제공하기, 18. axis label 폰트제공, 19. legend alpha조정 지원, 20 레이아웃 바꾸기, x축 위치 지정하기(sincos그래프),\
        #          21. fill below 도 0 기점으로 칠할건지 x축 기점으로 칠한건지 선택할 수 있어야 함.")
        
        

        


    





    # 사이드바 (3) - Chart
        chart=st.sidebar.markdown("# STEP1 : CHART 옵션 선택")                    
        # 1번. TITLE
        #TITLE=st.sidebar.markdown("# 1. 제목TITLE")
        with st.sidebar.expander("제목TITLE") :
            
            #title_markdown = st.markdown("### TITLE")
            title = st.text_input("Input Title of Graph", "Your Graph")
            title_size = st.number_input("title_size",min_value=0, value=20)       
            title_font =st.selectbox("Title Font", ['Arial','Calibri','Cambria','Comic Sans MS','Courier New','Georgia','Impact','Lucida Console','Lucida Sans Unicode','Microsoft Sans Serif','Palatino Linotype','Segoe UI','Tahoma','Times New Roman','Trebuchet MS','Verdana','Symbol','Webdings','Wingdings','MS Gothic'])
            title_weight = st.selectbox("Title Weight", ['normal', 'bold', 'semibold'])           
            title_style = st.selectbox("Title Style",['normal', 'italic'])                       
            title_color = st.selectbox("Title Color", ["black", "white","red", "blue","green", "yellow", "cyan","magenta", "gray"])
            title_pad = st.number_input("Title Pad", min_value=1, value=20)
            title_loc = st.selectbox("Title Location", ["center", "left", "right"])            
            title_h_location = st.slider("Title Horizontal Location", -1.0, 2.0, 0.5)
            title_v_location = st.slider("Title Vertical Location", -1.0, 2.0, 1.0)             
            title_va = st.select_slider("Title VerticalAlignment", ["top", "center", "bottom"],"center")
            title_ha = st.select_slider("Title HorizontalAlignment", ["left","center","right"],"center")
            title_bbox = st.checkbox("Title Background", False)
            if title_bbox is True:
                title_bbox_color = st.color_picker("Title Background Color")
                title_bbox_alpha = st.slider("Title Background Clarity", 0.0,1.0,1.0)
            else :
                 title_bbox_color = None
                 title_bbox_alpha = None

            title_stretch = st.select_slider("Title Stretch", ['ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'], 'normal')

            
        # 2번. LEGEND
        # LEGEND=st.sidebar.markdown("## 2. 범례LEGEND")
        with st.sidebar.expander("2. 범례LEGEND") :
            show_legend = st.checkbox("Show Legend", value=True)            
            if show_legend is True :
                legend_frameon = st.checkbox("Legend Frame On",False)
                legend_facecolor = st.selectbox("Legend Facecolor Color", ["white","black", "red", "blue","green", "yellow", "cyan","magenta", "gray"])
                legend_edgecolor = st.selectbox("Legend Edgecolor Color", ["white","black", "red", "blue","green", "yellow", "cyan","magenta", "gray"])
                legend_fontfamily = st.selectbox("Legend Font", ['Arial','Calibri','Cambria','Comic Sans MS','Courier New','Georgia','Impact','Lucida Console','Lucida Sans Unicode','Microsoft Sans Serif','Palatino Linotype','Segoe UI','Tahoma','Times New Roman','Trebuchet MS','Verdana','Symbol','Webdings','Wingdings','MS Gothic'])            
                legend_fontsize = st.number_input("Legend font size",7)
                legend_fontcolor = st.selectbox("Legend font Color", ["black", "white","red", "blue","green", "yellow", "cyan","magenta", "gray"])            
                legend_ncols = st.number_input("Legend Columns Number", 1,num_graphs,1)                
                legend_loc = st.selectbox("location",["upper left", "upper right", "upper center", "lower left", "lower center", "lower right", "center left", "center right", "Input Manually"])                
                if legend_loc == "Input Manually" :                    
                    legend_h_loc = st.slider("Legend Horizontal Location", -1.0, 2.0, 0.5)
                    legend_v_loc = st.slider("Legend Vertical Location", -1.0, 2.0, -0.1)

        # 3번. GRID
        # GRID = st.sidebar.markdown("## 3. 격자GRID")
        with st.sidebar.expander("3. 격자GRID") :
            grid = st.checkbox("Grid",True)       
            if grid is True :
                 grid_axis = st.selectbox("Grid Axis", ["both","x","y"])
                 grid_style = st.selectbox("Grid Style", ['-','--',':',"o"])
                 grid_color = st.selectbox("Grid Color", [ "gray", "black", "white","red", "blue","green", "yellow", "cyan","magenta"])
                 grid_clarity = st.slider("Grid Clarity", 0.0, 1.0, 0.5)   
                 grid_linewidth = st.number_input("Grid Linewidth", min_value=0.0, value=0.5)

        # 4번. FACECOLOR
        # FACECOLOR = st.sidebar.markdown("## 4. 배경색")
        with st.sidebar.expander("4. 배경색Facecolor") :
            back_plate = st.selectbox("Figure FaceColor", ['lightblue', 'white', 'gray', 'black'])
            back_plate_ax = st.selectbox("axes FaceColor", ['lightblue', 'white', 'gray', 'black'])

        
        with st.sidebar.expander("이미지크기 및 축표시figuresize & axis visible") :
            figure_width = st.number_input("Width",min_value=1, value=10)
            figure_height = st.number_input("Height",min_value=1, value=6)       

            
    ## STEP1 : 축 옵션 선택AXIS OPTION
        AXIS=st.sidebar.markdown("# STEP2 : 축 옵션 선택AXIS OPTION")   
        # 사이드바 (4) : AXIS

        y_min = df.min().min()
        y_max = df.max().max()
        y_mean = y_min + y_max / 2

        x_min = df.index[0]
        x_max = df.index[-1]
        x_mean = np.abs(x_max - x_min)
        x_minimum = x_min - x_mean
        x_maximum = x_max + x_mean 
        x_axis_range = pd.date_range(start=x_minimum, end=x_maximum) if index_datetime is True else range(x_minimum, x_maximum)
        # axis에는 숫자형과 날짜형만 올 수 있습니다.    
        
        with st.sidebar.expander("축AXIS") :
            st.markdown("### 축 표시axis visible")
            figure_axis_visble_top = st.checkbox("Top Axis Visible", True)            
            figure_axis_visble_bottom = st.checkbox("Bottom Axis Visible", True)            
            figure_axis_visble_left = st.checkbox("Left Axis Visible", True)            
            figure_axis_visble_right = st.checkbox("Right Axis Visible", True)    

            st.markdown("### 축 서식Axis Spine")
            xaxis_spine_color = st.selectbox("X axis spine Color", ["black", "white","red", "blue","green", "yellow", "cyan","magenta", "gray"])
            xaxis_spine_linewidth = st.number_input("X axis spine linewidth", 0.1,value=1.0)
            xaxis_spine_clarity = st.number_input("X axis spine clarity", 0.0,value=1.0)


            

         
        # x_axis_label = st.text_input("Input Title of Graph", "Your Graph")
        with st.sidebar.expander("X축 Xaxis") :
            st.markdown("### AXIS LABEL")
            xaxis_label = st.text_input("X axis Label","X")                    
            xaxis_size = st.number_input("X axis Label size",min_value=0,value=20)       
            xaxis_font = st.selectbox("X axis Label font", ['Arial','Calibri','Cambria','Comic Sans MS','Courier New','Georgia','Impact','Lucida Console','Lucida Sans Unicode','Microsoft Sans Serif','Palatino Linotype','Segoe UI','Tahoma','Times New Roman','Trebuchet MS','Verdana','Symbol','Webdings','Wingdings','MS Gothic'])
            xaxis_weight = st.selectbox("X axis Label Weight", ['normal', 'bold', 'semibold'])           
            xaxis_style = st.selectbox("X axis Label Style",['normal', 'italic'])                       
            xaxis_color = st.selectbox("X axis Label Color", ["black", "white","red", "blue","green", "yellow", "cyan","magenta", "gray"])
            xaxis_rotation = st.selectbox("X axis Label Rotation", [0,90,180,270])    
            xaxis_stretch = st.select_slider("X axis Label Stretch", ['ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'], 'normal')        
            xaxis_h_location = st.slider("X Label Label Horizontal Location", -1.0,1.0,0.5)
            xaxis_v_location = st.slider("X Label Label Vertical Location", -1.0,1.0,-0.2)
            
            st.markdown("### TICK MARKING")
            xticks_marking_width = st.number_input("X ticks marking width", 0.1,value=0.5)
            xtciks_marking_length = st.number_input("X ticks marking height", 0.1,value=3.0)
            xticks_marking_color = st.selectbox("X ticks marking color", ["black", "white","red", "blue","green", "yellow", "cyan","magenta", "gray"])

            st.markdown("### TICK LABEL")            
            xaxis_lim = st.select_slider("x axis label range", x_axis_range, (x_min, x_max))        
            xticks_label_number = st.selectbox("How many ticks?", ["Auto", "Not Visible", "Specific Num", "every"])
            if (xticks_label_number != "Auto") & (xticks_label_number != "Not Visible") :
                xticks_label_number_ = st.number_input("ㄴTick Label Number", 0,value=10)
            xticks_label_format = st.selectbox("X ticks Label Format", ["str","float","int","%","Date"])
            xticks_label_size = st.number_input("X ticks label size",10)       
            xticks_label_color = st.selectbox("X ticks label Color", ["black", "white","red", "blue","green", "yellow", "cyan","magenta", "gray"])
            xticks_label_rotation = st.selectbox("X ticks label Rotation", [0,90,180,270])    
            
        
        

        # x_axis_label = st.text_input("Input Title of Graph", "Your Graph")
        with st.sidebar.expander("Y축 YAxis") :
            yaxis_label = st.text_input("y axis Label","y")       
            yaxis_size = st.number_input("y axis_size Label",min_value=0,value=20)       
            yaxis_font = st.selectbox("y axis Label font", ['Arial','Calibri','Cambria','Comic Sans MS','Courier New','Georgia','Impact','Lucida Console','Lucida Sans Unicode','Microsoft Sans Serif','Palatino Linotype','Segoe UI','Tahoma','Times New Roman','Trebuchet MS','Verdana','Symbol','Webdings','Wingdings','MS Gothic'])
            yaxis_weight = st.selectbox("y axis Label Weight", ['normal', 'bold', 'semibold'])           
            yaxis_style = st.selectbox("y axis Label Style",['normal', 'italic'])                       
            yaxis_color = st.selectbox("y axis Label Color", ["black", "white","red", "blue","green", "yellow", "cyan","magenta", "gray"])
            yaxis_rotation = st.selectbox("y axis Label Rotation", [90,0,180,270])            
            yaxis_stretch = st.select_slider("y axis Label Stretch", ['ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'], 'normal')
            yaxis_h_location = st.slider("y Label Label Horizontal Location", -1.0,1.0,-0.10)
            yaxis_v_location = st.slider("y Label Label Vertical Location", -1.0,1.0,0.5)

            yticks_marking_width = st.number_input("y axis marking width", 0.1,value=0.5)
            ytciks_marking_length = st.number_input("y axis marking height", 0.1,value=3.0)
            yticks_marking_color = st.selectbox("y axis marking color", ["black", "white","red", "blue","green", "yellow", "cyan","magenta", "gray"])

            #yaxis_lim = st.slider("y axis range", y_min-y_mean, y_max+y_mean, (y_min, y_max))                   
            yticks_label_number = st.selectbox("y axis How many ticks?", ["Auto", "Not Visible", "Specific Num", "every"])
            if (yticks_label_number != "Auto") & (yticks_label_number != "Not Visible") :
                yticks_label_number_ = st.number_input("ㄴy axis Tick Label Number", 0,value=10)            
            yticks_label_size = st.number_input("y ticks label" ,10)       
            yticks_label_color = st.selectbox("y ticks label Color", ["black", "white","red", "blue","green", "yellow", "cyan","magenta", "gray"])
            yticks_label_rotation = st.selectbox("y ticks label Rotation", [0,90,180,270])    
            

    ## STEP1 : 축 옵션 선택AXIS OPTION
        DATA=st.sidebar.markdown("# STEP3 : 그래프 옵션 선택DATA(PLOT)")                 
        
        
    # 사이드바 (2) - Data + 본문(3) - 그래프 그리기 (2번. plot(DATA))
    
        size = (figure_width, figure_height)
        fig, ax = plt.subplots(figsize=size)

    # (2) - 1. 옵션선택란 만들기

        # 색깔 컨셉
        cmaps = [cmap for cmap in plt.cm.datad]
        _ = st.sidebar.markdown("### 컬러맵Colormap")
        graph_cmap = st.sidebar.selectbox("", cmaps)        
        colors = [rgba2hex(rgba) for rgba in eval("pl.cm."+graph_cmap+"(np.linspace(0,1,num_graphs))")]
        
        __ = st.sidebar.markdown("### 축별 옵션axis")        
        for i in range(num_graphs):            
                with st.sidebar.expander(f" ### Graph {i+1} : {labels[i]}") : 
                    label = labels[i]                
                    graph_label = st.text_input(f"Label for {label}", label)  
                    graph_color = st.color_picker(f"Color for {label}", colors[i])                                      
                    ### 직접입력시 필요함. 
                    # x_data = st.text_input(f"X Axis Data {i+1}", "1, 2, 3")
                    # y_data = st.text_input(f"Y Axis Data {i+1}", "4, 5, 6")
                    clarity = st.slider(f"Clarity {i+1}", 0.0, 1.0, 1.0)                      
                    graph_linewidth = st.slider(f"Line Width {i+1}", 1, 10, 2)                 


                    graph_linestyle = st.selectbox(f"Line Style {i+1}", ['-','--',':','-.','None'])
                    graph_capstyle = st.selectbox(f"CapStyle {i+1}",["round","butt","projecting","round"])
                    graph_jointstyle = st.selectbox(f"JointStyle {i+1}",["round","miter","bevel"])                    
                    graph_drawstyle = st.selectbox(f"DrawStyle {i+1}",["default","steps","steps-mid"])

                    graph_marker = st.checkbox(f"Marker {i+1}", False)
                    graph_marker_style = st.selectbox(f"Line Marker Style {i+1}", ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd'])                                       
                    graph_marker_size = st.slider(f"Marker Size {i+1}", 0.0,30.0,10.0)
                    graph_marker_every = st.number_input(f"Mark Every {i+1} :",int(1),int(len(df)),int(len(df)/20))
                    graph_marker_color = st.color_picker(f"Marker Color {i+1}", colors[i])
                    graph_marker_edgecolor = st.color_picker(f"Marker Edge Color {i+1}", colors[i])

                    graph_fill_between = st.checkbox(f"Fill Below {i+1}", False)
                    graph_fill_between_color = st.color_picker(f"Fill Below Color {i+1}", colors[i])
                    graph_fill_between_clarity = st.slider(f"Filling Clarity for {i+1}",0.0,1.0,0.5)

                    if graph_fill_between is True :
                         plt.fill_between(df.index, df[df.columns[i]], facecolor=graph_fill_between_color,
                                          alpha=graph_fill_between_clarity)
                
                    marker_dict = {"marker" : graph_marker_style if graph_marker is True else None,                  
                            "markerfacecolor" : graph_marker_color,
                            "markeredgecolor" : graph_marker_edgecolor,
                            "markersize" : graph_marker_size,
                            "markevery" : graph_marker_every}



                    df[df.columns[i]].plot(ax=ax,
                                           label=graph_label,
                                           alpha=clarity,
                                           linewidth=graph_linewidth,                                           
                                           linestyle = graph_linestyle,
                                           drawstyle = graph_drawstyle,
                                           c=graph_color, 
                                           **marker_dict )        
                    ax.lines[i].set_solid_capstyle(graph_capstyle)
                                           
                            

        
                     
    
        
    
    
    
        # 설정된 옵션들로 그래프 그리기

        #fig, ax = plt.subplots(figsize=(figure_width,figure_height))    
        #df.plot(ax=ax)
        fig.set_facecolor(back_plate)
        ax.set_facecolor(back_plate_ax)
        plt.grid(grid, axis=grid_axis,linestyle=grid_style, linewidth=grid_linewidth, color=grid_color, alpha=grid_clarity)
        
        
        
        
        if show_legend is True :
            
            if legend_loc == "Input Manually" :  
                legend = plt.legend(frameon=legend_frameon, facecolor=legend_facecolor, edgecolor=legend_edgecolor,ncol=legend_ncols)            
                legend.set_bbox_to_anchor((legend_h_loc, legend_v_loc))
            else :
                legend = plt.legend(loc=legend_loc, frameon=legend_frameon, facecolor=legend_facecolor, fontsize=legend_fontsize, ncol=legend_ncols)
            for i in range(len(legend.get_texts())):
                legend.get_texts()[i].set_fontfamily(legend_fontfamily)
                legend.get_texts()[i].set_color(legend_fontcolor)
                legend.get_texts()[i].set_fontsize(legend_fontsize)

        ax.spines['top'].set_visible(figure_axis_visble_top)
        ax.spines['bottom'].set_visible(figure_axis_visble_bottom)
        ax.spines['left'].set_visible(figure_axis_visble_left)
        ax.spines['right'].set_visible(figure_axis_visble_right)

        ax.spines['top'].set_color(xaxis_spine_color)
        ax.spines['bottom'].set_color(xaxis_spine_color)
        ax.spines['left'].set_color(xaxis_spine_color)
        ax.spines['right'].set_color(xaxis_spine_color)

        ax.spines['top'].set_linewidth(xaxis_spine_linewidth)
        ax.spines['bottom'].set_linewidth(xaxis_spine_linewidth)
        ax.spines['left'].set_linewidth(xaxis_spine_linewidth)
        ax.spines['right'].set_linewidth(xaxis_spine_linewidth)

        ax.spines['top'].set_alpha(xaxis_spine_clarity)
        ax.spines['bottom'].set_alpha(xaxis_spine_clarity)
        ax.spines['left'].set_alpha(xaxis_spine_clarity)
        ax.spines['right'].set_alpha(xaxis_spine_clarity)
        
                
                    
        title_font={"family" : title_font,
                "weight" : title_weight,
                "size" : title_size,
                "style" : title_style,
                "color" : title_color,
                "stretch" : title_stretch,          
                "bbox" : {"color" : title_bbox_color, "alpha" : title_bbox_alpha} if title_bbox is True else None              
                }
        title = plt.title(title, fontdict=title_font, loc=title_loc, pad=title_pad)
        title.set_position((title_h_location, title_v_location))
        
        
        # 축 라벨 서식
        x_axis_label_format = {
        'weight': xaxis_weight,
        'style': xaxis_style,
        'size': xaxis_size,
        'family': xaxis_font,
        'rotation' : xaxis_rotation,
        'color' : xaxis_color,
        'stretch' : xaxis_stretch
        }

        y_axis_label_format = {
        'weight' : yaxis_weight,
        'style' : yaxis_style,
        'size' : yaxis_size,
        'family' : yaxis_font,
        'rotation' : yaxis_rotation,
        'color' : yaxis_color,
        'stretch' : yaxis_stretch
        }

        xlabel_ = plt.xlabel(xaxis_label, fontdict=x_axis_label_format)
        xaxis = plt.gca().xaxis    
        xaxis.set_label_coords(xaxis_h_location, xaxis_v_location)


        ylabel_ = plt.ylabel(yaxis_label, fontdict=y_axis_label_format)
        yaxis = plt.gca().yaxis
        yaxis.set_label_coords(yaxis_h_location, yaxis_v_location)


        # 눈금과 눈금라벨 


        from matplotlib import ticker

        # x axis tick label.
        xticks_label_func = "ax.xaxis.set_major_locator"    
        xticks_label_options = [ticker.NullLocator,
                                ticker.LinearLocator,
                                ticker.MultipleLocator]
        n = ["Auto", "Not Visible", "Specific Num", "every"].index(xticks_label_number)-1
                                
        if xticks_label_number != "Auto" :
            if xticks_label_number == "Not Visible" :
                ax.xaxis.set_major_locator(ticker.NullLocator())
            else :           
                eval(xticks_label_func)(xticks_label_options[n](xticks_label_number_))

        # y axis tick label 
        yticks_label_func = "ax.yaxis.set_major_locator"    
        yticks_label_options = [ticker.NullLocator,
                                ticker.LinearLocator,
                                ticker.MultipleLocator]
        n = ["Auto", "Not Visible", "Specific Num", "every"].index(yticks_label_number)-1
                                
        if yticks_label_number != "Auto" :
            if yticks_label_number == "Not Visible" :
                ax.yaxis.set_major_locator(ticker.NullLocator())
            else :           
                eval(yticks_label_func)(yticks_label_options[n](yticks_label_number_))


                                

                



        x_ticks_label_format = {
        'labelsize': xticks_label_size,
        'labelrotation' : xticks_label_rotation,
        'labelcolor' : xticks_label_color
        }

        x_ticks_marking_format = {
        'color': xticks_marking_color,
        'length' : xtciks_marking_length,
        'width' : xticks_marking_width
        }

        y_ticks_marking_format = {
        'color': yticks_marking_color,
        'length' : ytciks_marking_length,
        'width' : yticks_marking_width
        }

        y_ticks_label_format = {
        'labelsize' : yticks_label_size,
        'labelrotation' : yticks_label_rotation,
        'labelcolor' : yticks_label_color
        }

        ax.tick_params(axis='x', which='major', **x_ticks_marking_format, **x_ticks_label_format)
        ax.tick_params(axis='y', which='major', **y_ticks_marking_format, **y_ticks_label_format)
        
    
        ### 축 범위       
        plt.xlim(xaxis_lim)
        #plt.ylim(yaxis_lim)





        
        




        # 데이터 직접 입력하는 경우 그래프 몇개 그릴지 확인
        ### Get user input for number of graphs to plot
        ### num_graphs = st.sidebar.number_input("Number of Graphs to Plot", min_value=1)
        
        # labeling 방법 (2) : dict에 포함시키기.
        # names = [next(name_gen) for i in range(num_graphs)]
        # a = {names[i] : st.text_input(f"graph{i}", value=names[i]) for i in range(num_graphs)}


        # Get user input for showing legend
        

            

        # 개별 그래프 정보입력란 생성
        # For each graph, get user input for data, title, color, and linewidth
        
        # names = [next(name_gen) for i in range(num_graphs)]
        # 
        # # labeling방법(1) : global 변수 생성방법
        # for i in range(num_graphs) :
        #     globals()[names[i]] = st.text_input(f"{names[i]}")


            
            
        
                

            # Convert comma-separated string data to list of float values
        #    x_data = [float(x) for x in x_data.split(",")]
        #    y_data = [float(y) for y in y_data.split(",")]
    #
        #    # Plot the graph using user inputs
        #    plot_graph(ax, 
        #               x_data, 
        #               y_data, 
        #               graph_title, 
        #               graph_color, 
        #               graph_linewidth, 
        #               show_legend, 
        #               label)

        # Show the final plot
        # st.pyplot(fig)
        
        st.write("# Your Figure :")
        st.pyplot(fig)

        st.header("Your Data :")
        st.write(df)


        st.write("# Save Figure?")
        save_pad = st.selectbox("여백pad", ["tight","wide","slim"])
        save_pad_ = ["tight","None","0"]    
        save_name = st.text_input("저장이름SaveName", "title")
        save_format = st.selectbox("저장형식format", [".pdf",".png"])
        save_resolution = st.number_input("해상도dpi", min_value=100, value=100)
        save_name_ = save_name+save_format

        
        if st.button("FIGURE DOWNLOAD"):        
            fig.savefig(save_name_, bbox_inches=save_pad_[["tight","wide","slim"].index(save_pad)], pad_inches=0, dpi=save_resolution)
    
if __name__ == '__main__':
    
    main()


    

