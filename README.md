# 拍拍贷风控分析

数据来自拍拍贷真实业务数据，从2015-01-01到2017-01-30的所有信用标的10%案例样本。数据集包含标的特征表数据和标的还款计划和还款记录表数据。

## :fire:PPD_LOAN_CHARACTERISTICS

<span style="font-size:18px; font-family: 'STSong'; color: purple; font-weight: bold;">1、数据表名称：标的特征表</span>

| 字段名                  | 中文字段         | 字段类型       | 中文说明                             |
| ----------------------- | ---------------- | -------------- | ------------------------------------ |
| LISTINGID               | 序列号           | int64          | 列表序号                             |
| LOAD_MONEY              | 借款金额         | int64          | 列表成交总金额                       |
| LOAN_TERM               | 借款期限         | int64          | 总的期数（按月计）                   |
| LOAN_RATE               | 借款利率         | float64        | 年化利率（百分数）                   |
| LOAN_FUNDING_DATE       | 借款成功日期     | datetime64[ns] | 列表成交的日期                       |
| INITIAL_RATING          | 初始评级         | object         | 列表成交时的信用评级                 |
| LOAN_TYPE               | 借款类型         | object         | 借款类型                             |
| IS_FIRST_INVEST         | 是否首标         | object         | 该标是否为借款人首标                 |
| AGE                     | 年龄             | int64          | 借款人在该列表借款成功时的年龄       |
| SEX                     | 性别             | object         | 该列表借款人性别                     |
| IS_PHONE                | 手机认证         | object         | 该列表借款人手机实名认证是否成功     |
| IS_RESIDENCE            | 户口认证         | object         | 该列表借款人户口认证是否成功         |
| IS_VIDEO                | 视频认证         | object         | 该列表借款人视频认证是否成功         |
| IS_EDU                  | 学历认证         | object         | 该列表借款人学历认证是否成功         |
| IS_CREDIT               | 征信认证         | object         | 该列表借款人征信认证是否成功         |
| IS_TAOBAO               | 淘宝认证         | object         | 该列表借款人淘宝认证是否成功         |
| SUCCESS_LOAN_NUMBER     | 历史成功借款次数 | int64          | 借款人在该列表成交之前的借款成功次数 |
| SUCCESS_LOAN_AMOUNT     | 历史成功借款金额 | int64          | 借款人在该列表成交之前的借款成功金额 |
| TOTAL_NEED_AMOUNT       | 总待还本金       | float64        | 借款人在该列表成交之前待还本金金额   |
| HISTORY_NORMAL_PAY_TERM | 历史正常还款期数 | int64          | 借款人在该列表成交之前的按期还款期数 |
| OVERDUE_TERM            | 历史逾期还款期数 | int64          | 借款人在该列表成交之前的逾期还款期数 |

<span style="font-size:18px; font-family: 'STSong'; color: purple; font-weight: bold;">2、数据概况：</span>标的特征表，每支标一条记录。共有21个字段，包括一个主键（listingid）、7个标的特征和13个成交当时的借款人信息，全部为成交当时可以获得的信息。

<span style="font-size:18px; font-family: 'STSong'; color: purple; font-weight: bold;">3、数据解读：</span>

- 序列号：为列表的唯一键。
- 初始评级：AAA为安全标，AA为赔标，A-F为信用等级。数据中不存在AAA和AA。
- 借款类型：应收安全标、电商、APP闪电、普通、其他。数据中不存在应收安全标。
- 学历认证：成功则表示有大专及以上学历，否则为大专以下学历。
- 征信认证：成功则表示有人行征信报告，否则为征信白户。
- 淘宝认证：成功则表示为淘宝店主。

## :fire:PPD_LOAN_PERIODIC

<span style="font-size:18px; font-family: 'STSong'; color: purple; font-weight: bold;">1、数据表名称：标的还款计划和还款记录表</span>

| 字段名            | 中文字段 | 字段类型       | 中文说明                     |
| ----------------- | -------- | -------------- | ---------------------------- |
| LISTINGID         | 列表Id   | int64          | 列表Id，主键                 |
| TERM              | 期数     | int64          | 期数Id，主键                 |
| PAY_STATUS        | 还款状态 | int64          | 到记录日的当期状态           |
| PAYABLE_PRINCIPAL | 应还本金 | float64        | 当期计划还款本金部分         |
| PAYABLE_INTEREST  | 应还利息 | float64        | 当期计划还款利息部分         |
| RESIDUE_PRINCIPAL | 剩余本金 | float64        | 到记录日，仍未还清的当期本金 |
| RESIDUE_INTEREST  | 剩余利息 | float64        | 到记录日，仍未还清的当期利息 |
| EXPIRATION_DATE   | 到期日期 | datetime64[ns] | 当期应还款日                 |
| PAY_DATE          | 还款日期 | object         | 当期最近一次实际还款日期     |
| RECORDDATE        | 记录日   | datetime64[ns] | 记录日                       |

<span style="font-size:18px; font-family: 'STSong'; color: purple; font-weight: bold;">2、数据概况：</span>标的还款计划和还款记录表，每支标每期还款为一条记录。 还款记录和状态更新至2017年2月22日。共有10个字段，包括两个主键（listingid和期数），3个还款计划字段和4个还款状态字段。

<span style="font-size:18px; font-family: 'STSong'; color: purple; font-weight: bold;">3、数据解读：</span>

- 列表Id：主键。
- 期数：主键。

## :fire:PPD_LOAN_CHAR_INVEST_STATUS

<span style="font-size:18px; font-family: 'STSong'; color: purple; font-weight: bold;">1、数据表名称：成交标的记录表</span>

| 字段名                   | 中文字段         | 字段类型 | 字段分类 | 中文说明                             |
| ------------------------ | ---------------- | -------- | -------- | ------------------------------------ |
| ListingId                | 列表序号         | int64    | 成交特征 | 列表序号                             |
| LOAD_MONEY               | 借款金额         | int64    | 成交特征 | 列表成交总金额                       |
| LOAN_TERM                | 借款期限         | int64    | 成交特征 | 总的期数（按月计）                   |
| LOAN_RATE                | 借款利率         | float64  | 成交特征 | 年化利率（百分数）                   |
| LOAN_FUNDING_DATE        | 借款成功日期     | object   | 成交特征 | 列表成交的日期                       |
| INITIAL_RATING           | 初始评级         | object   | 成交特征 | 列表成交时的信用评级                 |
| LOAN_TYPE                | 借款类型         | object   | 成交特征 | 借款类型                             |
| IS_FIRST_INVEST          | 是否首标         | object   | 成交特征 | 该标是否为借款人首标                 |
| AGE                      | 年龄             | int64    | 成交特征 | 借款人在该列表借款成功时的年龄       |
| SEX                      | 性别             | object   | 成交特征 | 该列表借款人性别                     |
| IS_PHONE                 | 手机认证         | object   | 成交特征 | 该列表借款人手机实名认证是否成功     |
| IS_RESIDENCE             | 户口认证         | object   | 成交特征 | 该列表借款人户口认证是否成功         |
| IS_VIDEO                 | 视频认证         | object   | 成交特征 | 该列表借款人视频认证是否成功         |
| IS_EDU                   | 学历认证         | object   | 成交特征 | 该列表借款人学历认证是否成功         |
| IS_CREDIT                | 征信认证         | object   | 成交特征 | 该列表借款人征信认证是否成功         |
| IS_TAOBAO                | 淘宝认证         | object   | 成交特征 | 该列表借款人淘宝认证是否成功         |
| SUCCESS_LOAN_NUMBER      | 历史成功借款次数 | float64  | 成交特征 | 借款人在该列表成交之前的借款成功次数 |
| SUCCESS_LOAN_AMOUNT      | 历史成功借款金额 | float64  | 成交特征 | 借款人在该列表成交之前的借款成功金额 |
| TOTAL_NEED_AMOUNT        | 总待还本金       | float64  | 成交特征 | 借款人在该列表成交之前待还本金金额   |
| HISTORY_NORMAL_PAY_TERM  | 历史正常还款期数 | int64    | 成交特征 | 借款人在该列表成交之前的按期还款期数 |
| OVERDUE_TERM             | 历史逾期还款期数 | int64    | 成交特征 | 借款人在该列表成交之前的逾期还款期数 |
| INVEST_AMOUNT            | 我的投资金额     | int64    | 成交特征 | 该投资人对该列表的投资金额           |
| CURRENT_BD_TERM          | 当前到期期数     | int64    | 当期特征 | 该列表当前应还的期数                 |
| CURRENT_PAYED_TERM       | 当前还款期数     | int64    | 当期特征 | 该列表已经成功还款的期数             |
| REPAID_PRINCIPAL         | 已还本金         | float64  | 当期特征 | 已经向该投资人成功还款的本金总额     |
| REPAID_INTEREST          | 已还利息         | float64  | 当期特征 | 已经向该投资人成功还款的利息总额     |
| REPAIR_PAYABLE_PRINCIPAL | 待还本金         | float64  | 当期特征 | 还需向该投资人还款的本金总额         |
| REPAIR_PAYABLE_INTEREST  | 待还利息         | float64  | 当期特征 | 还需向该投资人还款的利息总额         |
| CURRENT_OVERDUE_DAYS     | 标当前逾期天数   | int64    | 当期特征 | 当期逾期天数。未逾期则为0            |
| CURRENT_STATUS           | 标当前状态       | object   | 当期特征 | 当期状态。                           |
| LAST_PAY_DATE            | 上次还款日期     | object   | 当期特征 | 上一次实际还款日期                   |
| LAST_PAY_PRINCIPAL       | 上次还款本金     | float64  | 当期特征 | 上一次实际向该投资人还款本金         |
| LAST_PAY_INTEREST        | 上次还款利息     | float64  | 当期特征 | 上一次实际向该投资人还款利息         |
| NEXT_PAYABLE_DATE        | 下次计划还款日期 | object   | 当期特征 | 下一次计划还款日期                   |
| NEXT_PAYABLE_PRINCIPAL   | 下次计划还款本金 | float64  | 当期特征 | 下一次计划向该投资人还款本金         |
| NEXT_PAYABLE_INTEREST    | 下次计划还款利息 | float64  | 当期特征 | 下一次计划向该投资人还款利息         |
| RECORDDATE               | 记录日期         | object   | 当期特征 | 一般为月末最后一天                   |

<span style="font-size:18px; font-family: 'STSong'; color: purple; font-weight: bold;">2、数据概况：</span>数据包含了该客户投资的从2015年1月1日起成交的所有标。以6个月月底的最后一天（2016年9月30日，2016年10月31日，2016年11月30日，2016年12月31日，2017年1月31日，2017年2月28日）作为recorddate，对每一个recorddate都提供了该客户投资的从2015年1月1日起到当天成交的所有标的数据，包括这些标成交时的特点（Loan Characteristics）、该客户投资的金额以及截至当天的收款情况（Investment Status）。

- LC部分共有21个字段，包括一个主键（listingid）、7个标的特征和13个成交当时的借款人信息，全部为成交当时可以获得的信息。
- IS部分有15个字段，包括截至recorddate当天标的还款状态，针对这位客户的已还和待还金额，最近的还款情况和下一期还款计划。

<span style="font-size:18px; font-family: 'STSong'; color: purple; font-weight: bold;">3、数据解读：</span>

- 列表序号：列表的唯一键。
- 借款成功日期：都在2015年1月1日以后。
- 初始评级：AAA为安全标，AA为赔标，A-F为信用等级。
- 借款类型：应收安全标、电商、APP闪电、普通、其他。
- 学历认证：成功则表示有大专及以上学历，否则表示大专以下学历。
- 征信认证：成功则表示有人行征信报告，否则表示人行征信白户。
- 淘宝认证：成功则表示为淘宝店主，否则表示为非淘宝店主。
- 标当前状态：正常还款中、逾期中、已还清、已债转。
- 















