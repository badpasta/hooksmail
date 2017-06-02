# Overview
	This is a simple scripts of create and update user information in staffdb.

# Changlog
### 2017-05-30 version: 0.1.8
	1. 修复了数据查重中大小写注意问题.
	2. 修复了staffdb中"email"字段后缀错误导致用户状态离职的问题.(理论上邮箱前缀具有唯一性, 但主要根据staffdb表中email字段不可重复属性设计.)
	3. 打开了time sleep开关.
	4. 增加了extenduser中测试是否在职的代码(已注释).

