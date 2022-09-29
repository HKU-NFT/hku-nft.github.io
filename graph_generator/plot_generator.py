import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import pathlib
from os import path

#########################(T1A)############################################
root_dir = path.join(pathlib.Path(__file__).parent.resolve(),'graph_data')
#bar/line chart(trade count)
data_path = path.join(root_dir,'T1A.csv')
bar_df = pd.read_csv(data_path, index_col = False)
bar_df['Txn'] = bar_df['Txn'].apply(lambda x : round(x*100,2))
#create bar
fig_0 = px.line(x = bar_df['Tc'], y = bar_df['Txn'], title="Trade count for NFT")
fig_0.add_scatter(x = bar_df['Tc'], y = bar_df['Txn'],name = "Trade count percentage trend")
fig_0.add_bar(x = bar_df['Tc'], y = bar_df['Txn'], name = "Trade count percentage distribution")
fig_0.update_traces(textfont_size=20, hovertemplate='Percentage on all traded tokens: %{y} <br>Number of trade: %{x} <extra></extra>')
fig_0.update_layout(yaxis={'title':'Percentage'},
                xaxis={'title':'Trade count'},
                showlegend=False)
#fig_0.show()

######################(T1B)#################################################
data_path = path.join(root_dir, 'T1B.csv')
line_df = pd.read_csv(data_path)
df_1 = line_df.loc[:, '1':'10'].apply(lambda x : round(x,2))
fig_1 = go.Figure()
for i in range(10):
    fig_1.add_trace(go.Line(x = line_df['max_Txn'],y= df_1.iloc[i], name = "Traded "+str(i+1)+" times"))
fig_1.update_layout(title="Token averaged price conditional on been traded",
                    xaxis={"title":"Trade Count"},
                    yaxis={"title": "Token Average Price"})
fig_1.update_traces(textfont_size=20, hovertemplate='Average price: %{y} <br>Number of trade: %{x} th <extra></extra>')
#fig_1.show()
####################(T1C)############################################################
data_path = path.join(root_dir, 'T1C_Win.csv')
df_win = pd.read_csv(data_path).loc[:,'1':'9'].apply(lambda x : round(x,2))
df_win.fillna('', inplace=True)
#heatmap(wining probability)
trade_count = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
trade_count_after_buy_in = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th"]
fig_2 = go.Figure()
fig_2.add_trace(go.Heatmap(z=df_win,x=trade_count_after_buy_in, y=trade_count, hoverongaps=False, name="Wining probability"))
fig_2.update_layout(title="Winning probability conditional on been trade",
                    xaxis={"title":"Number of trade after initial buy in"},
                    yaxis={"title": "Total trade count (including initial buy in)"})
fig_2.update_traces(text=df_win,
                    texttemplate="%{text}",
                    hovertemplate='Total trade count (including initial buy in): %{y} <br>Number of trade after initial buy in: %{x} th <br>Wining probability: %{z} <extra></extra>')
#fig_2.show()

#heatmap(gross return)
trade_count = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
trade_count_after_buy_in = ["1st","2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th"]
df_return = pd.read_csv(path.join(root_dir, 'T1C_Return.csv')).loc[1:,'2':'10'].apply(lambda x : round(x, 2))
df_return.fillna('', inplace=True)
fig_3 = go.Figure()
fig_3.add_trace(go.Heatmap(z=df_return,x=trade_count_after_buy_in, y=trade_count, hoverongaps=False))
fig_3.update_layout(title="Token average gross return",
                    xaxis={"title":"Number of trade after initial buy in"},
                    yaxis={"title": "Total trade count (including initial buy in)"})
fig_3.update_traces(text=df_return,
                    texttemplate="%{text}",
                    hovertemplate='Total trade count (including initial buy in): %{y} <br>Number of trade after initial buy in: %{x} th <br>Gross return: %{z} <extra></extra>')
#fig_3.show()

#########################(T2A)####################################
data_path = path.join(root_dir, 'T2A.csv')
df_2a = pd.read_csv(data_path)
df_2a = df_2a[df_2a.day >"2018/1/1"]
#timeline = set(df_2a['day'].apply(lambda x : x[:-3]).to_list)
fig_4 = make_subplots(specs=[[{"secondary_y": True}]])
fig_4.add_trace(go.Scatter(x = df_2a['day'], y = df_2a['Proj_traded'], name = "Number of project traded", mode = "lines"), secondary_y=False)
fig_4.add_trace(go.Scatter(x = df_2a['day'], y = df_2a['Token_traded'], name = "Number of token traded", mode = "lines"),secondary_y=True)
fig_4.update_layout(title = "Number of project/token traded",
                    xaxis = {"title":"Time"})
fig_4.update_yaxes(title_text="Project traded amount", secondary_y=False)
fig_4.update_yaxes(title_text="Token traded amount", secondary_y=True)
fig_4.update_traces(textfont_size = 20, hovertemplate = "Time: %{x}<br> Traded amount: %{y} <extra></extra>")
#fig_4.show()
#####chart for trade probability
df_prob = df_2a.loc[:,"trade_7d":"trade_365d"]*100
fig_5 = go.Figure()
for column in df_prob.columns.to_list()[:-1]:
        fig_5.add_trace(go.Scatter(x = df_2a['day'], y = df_prob[column], mode='lines', stackgroup='one', name = column))
fig_5.update_traces(visible=False)
fig_5.add_trace(go.Scatter(x = df_2a['day'], y = df_prob["trade_365d"], mode='lines', stackgroup='one', name = "trade_365d"))
fig_5.update_traces(textfont_size = 20, hovertemplate='Trade probability: %{y}<br> Date: %{x} <extra></extra>')
fig_5.update_layout(title = "Trade Probability at Specific Time",
                    xaxis = {"title":"Time"},
                    yaxis = {"title":"Trade Probability(%)"},
                    updatemenus=[go.layout.Updatemenu(
                        active=0,
                        buttons=list(
                            [dict(label = 'One year',
                                 method = 'update',
                                 args = [{'visible': [False, False, False, False, True]},
                                         {'title': 'Trade in 365 Days'},
                                         {'showlegend':True}]),
                            dict(label = 'Half year',
                                 method = 'update',
                                 args = [{'visible': [False, False, False, True, False]},
                                         {'title': 'Trade in 182 Days'},
                                         {'showlegend':True}]),
                            dict(label = 'One quarter',
                                 method = 'update',
                                 args = [{'visible': [False, False, True, False, False]},
                                         {'title': 'Trade in 91 Days'},
                                         {'showlegend':True}]),
                            dict(label = 'Half month',
                                 method = 'update',
                                 args = [{'visible': [False, True, False, False, False]},
                                         {'title': 'Trade in 14 Days'},
                                         {'showlegend':True}]),
                            dict(label = 'One week',
                                 method = 'update',
                                 args = [{'visible': [True, False, False, False, False]},
                                         {'title': 'Trade in 7 Days'},
                                         {'showlegend':True}])])
                    )])

#fig_5.show()
##########################(T2C)######################################
data_path = path.join(root_dir,'T2B.csv')
df_2c = pd.read_csv(data_path)
df_2c = df_2c[df_2c.day > "2018/1/1"]
fig_6 = go.Figure()
y_data = df_2c['N1/N'].rolling(7).mean()*100
fig_6.add_trace(go.Scatter(x = df_2c['day'], y = y_data))
fig_6.update_traces(hovertemplate="Turnover: %{y} <br> Date: %{x} <extra></extra>")
fig_6.update_layout(title="Percentage of First-time Traded token",
                    xaxis = {"title":"Time"},
                    yaxis = {"title":"Percentage(%)"})
#fig_6.show()

##################Export HTML##########################################
with open('chart.html', 'a') as f:
    f.write(fig_0.to_html(full_html=False, include_plotlyjs='cnd'))
    f.write(fig_1.to_html(full_html=False, include_plotlyjs='cnd'))
    f.write(fig_2.to_html(full_html=False, include_plotlyjs='cnd'))
    f.write(fig_3.to_html(full_html=False, include_plotlyjs='cnd'))
    f.write(fig_4.to_html(full_html=False, include_plotlyjs='cnd'))
    f.write(fig_5.to_html(full_html=False, include_plotlyjs='cnd'))
    f.write(fig_6.to_html(full_html=False, include_plotlyjs='cnd'))