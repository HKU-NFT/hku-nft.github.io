import plotly.express as px
import plotly.graph_objects as go
#pie chart(trade count)
value = [0.426,0.282, 0.158, 0.0794, 0.0341, 0.0126, 0.005, 0.0029]
label = ["Traded once", "Traded twice", "Trade 3 times", "Traded 4 times", "Traded 5 times", "Traded 6 times", "Traded 7 times", "Traded 8+ times"]
fig = px.pie(values = value, names = label, labels = label, title="Trade count for NFT")
fig.update_traces(textposition='inside', textinfo='percent+label', textfont_size=20)
#fig.write_html('text.html')

#heatmap(wining probability)
trade_count = ["Traded once", "Traded twice", "Trade 3 times", "Traded 4 times", "Traded 5 times", "Traded 6 times", "Traded 7 times", "Traded 8 times", "Traded 9 times", "Traded 10 times", "Traded more than 10 times"]
trade_count_after_buy_in = ["1st trade", "2nd trade", "3rd trade", "4th trade", "5th trade", "6th trade", "7th trade", "8th trade", "9th trade", "10th trade", ">10th trade"]
wining_probability = [[None,0.54,0.66,0.71,0.74,0.75,0.76,0.77,0.78,0.79,0.75],
                    [None, None, 0.50, 0.61, 0.67, 0.70, 0.72, 0.74, 0.75, 0.74, 0.70],
                    [None, None, None, 0.49,0.59, 0.65, 0.67, 0.71, 0.73, 0.71, 0.68],
                    [None, None, None, None, 0.48, 0.58, 0.64, 0.65, 0.68, 0.69, 0.69],
                    [None, None, None, None, None, 0.49, 0.57, 0.62, 0.64, 0.65, 0.60],
                    [None, None, None, None, None, None, 0.49, 0.55, 0.61, 0.60, 0.64],
                    [None, None, None, None, None, None, None, 0.47, 0.58, 0.57, 0.61],
                    [None, None, None, None, None, None, None, None, 0.48, 0.52, 0.60],
                    [None, None, None, None, None, None, None, None, None, 0.49, 0.59],
                    [None, None, None, None, None, None, None, None, None, None, 0.54]]
fig_1 = go.Figure()
fig_1.add_trace(go.Heatmap(z=wining_probability,x=trade_count_after_buy_in, y=trade_count, hoverongaps=False))
fig_1.update_layout(title="Winning probability conditional on been trade",
                    xaxis={"title":"Number of trade afer initial buy in"},
                    yaxis={"title": "Total trade count (including initial buy in)"})
#fig_1.show()
#fig_1.write_html('text.html')
#heatmap(gross return)
trade_count = ["Traded once", "Traded twice", "Trade 3 times", "Traded 4 times", "Traded 5 times", "Traded 6 times", "Traded 7 times", "Traded 8 times", "Traded 9 times", "Traded 10 times", "Traded more than 10 times"]
trade_count_after_buy_in = ["1st trade", "2nd trade", "3rd trade", "4th trade", "5th trade", "6th trade", "7th trade", "8th trade", "9th trade", "10th trade", ">10th trade"]
gross_return = [[None, None, None, None, None, None, None, None, None, None, None],
[1.49, None, None, None, None, None, None, None, None, None, None],
[1.53, 1.35, None, None, None, None, None, None, None, None, None],
[1.59, 1.42, 1.32, None, None, None, None, None, None, None, None],
[1.62, 1.46, 1.38, 1.28, None, None, None, None, None, None, None],
[1.63, 1.52, 1.43, 1.34, 1.22, None, None, None, None, None, None],
[1.65, 1.49, 1.46, 1.33, 1.26, 1.19, None, None, None, None, None],
[1.61, 1.52, 1.45, 1.33, 1.33, 1.27, 1.19, None, None, None, None],
[1.31, 1.39, 1.38, 1.37, 1.33, 1.23, 1.19, 1.12, None, None, None],
[1.04, 1.09, 1.14, 1.20, 1.40, 1.17, 1.46, 1.08, 1.05, None, None],
[5.15, 1.04, 1.16, 1.19, 1.11, 1.15, 0.99, 1.17, 1.00, 1.07, None]]
fig_2 = go.Figure()
fig_2.add_trace(go.Heatmap(z=gross_return,x=trade_count_after_buy_in, y=trade_count, hoverongaps=False))
fig_2.update_layout(title="Token average gross return",
                    xaxis={"title":"Number of trade afer initial buy in"},
                    yaxis={"title": "Total trade count (including initial buy in)"})
#fig_2.show()
fig_2.write_html('text.html')