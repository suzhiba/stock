import tushare as ts
import pandas
import os
#stock data , refer to http://tushare.org/reference.html (can use google translate, if something difficult to understand,contact me)
#sometimes, this programming will be time out.Re-run it.
#if any bug, mail me hust.cs.suzhiba@gmail.com

#python file path
dirName = os.getcwd()

print dirName
'''
	company data like performance , profit and so on.
	performance:code, the code
''' 
df=ts.get_stock_basics()
df.to_excel(dirName+'/data/fundamentalData/'+'basics.xlsx')
for years in [2014,2015]:
	for season in range(4): 
		df=ts.get_report_data(years,season+1)
		df.to_excel(dirName+'/data/fundamentalData/'+'preformance_report_'+str(years)+'_'+str(season+1)+'.xlsx')
		df=ts.get_profit_data(years,season+1)
		df.to_excel(dirName+'/data/fundamentalData/'+'profit_'+str(years)+'_'+str(season+1)+'.xlsx')
		df=ts.get_operation_data(years,season+1)
		df.to_excel(dirName+'/data/fundamentalData/'+'operation_ability'+str(years)+'_'+str(season+1)+'.xlsx')
		df=ts.get_growth_data(years,season+1)
		df.to_excel(dirName+'/data/fundamentalData/'+'growth_ability'+str(years)+'_'+str(season+1)+'.xlsx')
		df=ts.get_debtpaying_data(years,season+1)
		df.to_excel(dirName+'/data/fundamentalData/'+'debtpaying_ability'+str(years)+'_'+str(season+1)+'.xlsx')
		df=ts.get_cashflow_data(years,season+1)
		df.to_excel(dirName+'/data/fundamentalData/'+'cashflow'+str(years)+'_'+str(season+1)+'.xlsx')

'''
economy data like GDP and bank rate and so on.
'''
df=ts.get_deposit_rate()
df.to_excel(dirName+'/data/economicData/'+'deposit_rate.xlsx')
df=ts.get_loan_rate()
df.to_excel(dirName+'/data/economicData/'+'loan_rate.xlsx')
df=ts.get_rrr()
df.to_excel(dirName+'/data/economicData/'+'requredReserve_rate.xlsx')
df=ts.get_money_supply()
df.to_excel(dirName+'/data/economicData/'+'money_supply.xlsx')
#money supply in the end of year
df=ts.get_money_supply_bal()
df.to_excel(dirName+'/data/economicData/'+'money_supply_bal.xlsx')
df=ts.get_gdp_year()
df.to_excel(dirName+'/data/economicData/'+'GDP_year.xlsx')
df=ts.get_gdp_quarter()
df.to_excel(dirName+'/data/economicData/'+'GDP_quater.xlsx')
#3 demand for gdp 
df=ts.get_gdp_for()
df.to_excel(dirName+'/data/economicData/'+'GDP_for.xlsx')
df=ts.get_cpi()
df.to_excel(dirName+'/data/economicData/'+'CPI.xlsx')
df=ts.get_ppi()
df.to_excel(dirName+'/data/economicData/'+'PPI.xlsx')


'''
this data means stock price plus loss of dividend
'''
code_right=['300417','002739']
for i in code_right:
	df=ts.get_h_data('300417', start='2014-01-01', end='2016-01-01')
	df.to_excel(dirName+'/data/hisWithrights offering/'+str(i)+'.xlsx', startrow=0,startcol=0)
	#all data use df = ts.get_stock_basics()


'''
	data for investment
'''
#high divedent (means optimistic for stock)
df = ts.profit_data(top=60)
df.sort('shares',ascending=False)
df.to_excel(dirName+'/data/investData/high_divedent.xlsx')

#performance prediction
df=ts.forecast_data(2016,2)

#stocks held by fundations(means optimistic for stock)

for years in [2014,2015]:
	for season in range(4): 
		df=ts.fund_holdings(years, season+1)
		df.to_excel(dirName+'/data/investData/'+'fund_hoding'+str(years)+'_'+str(season+1)+'.xlsx')


#margin trading (shanghai)
df=ts.sh_margins(start='2014-01-01', end='2016-01-01')
df.to_excel(dirName+'/data/investData/'+'margin_trading_sh.xlsx')
df=ts.sh_margin_details(start='2014-01-01', end='2016-01-01', symbol='601989')
df.to_excel(dirName+'/data/investData/'+'detail_margin_trading_sh.xlsx')

#margin trading (shanghai)
df=ts.sz_margins(start='2014-01-01', end='2016-01-01')
df.to_excel(dirName+'/data/investData/'+'margin_trading_sz.xlsx')



''' 
Interbank Offered(bank borrow money form anathor bank
'''
df = ts.shibor_data(2015)
df.sort('date', ascending=False).head(10)
df.to_excel(dirName+'/data/interbankData/'+'inter_rate.xlsx')
