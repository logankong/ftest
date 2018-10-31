from ftest import *


class JianceElement(Base):
    tbodyTag = (By.TAG_NAME, 'tbody')
    lineTag = (By.TAG_NAME, 'tr')
    checkboxClass = (By.CSS_SELECTOR, 'input.checkbox')
    valueTag = (By.TAG_NAME, 'input')
    refreshJs = '''return  new DM.timer(function(){
                                vm.initData();alert('123');
                            });'''

    def getSql(self, group_id, host_id):
        self.db = DB()
        # 漏洞扫描事件数
        scanNum = self.db.getOne(
            "SELECT count(*) as num  FROM q_event WHERE group_id = %s AND host_id = %s AND type = 'scan' and status =0", (group_id, host_id))
        scanNum = str(scanNum.get('num'))
        # 威胁情报事件数
        vulnewsNum = self.db.getOne(
            "SELECT count(*) as num FROM q_event WHERE group_id = %s AND host_id = %s AND type = 'vulnews' and status =0", (group_id, host_id))
        vulnewsNum = str(vulnewsNum.get('num'))
        # 内容变更事件数
        contenthangeNum = self.db.getOne(
            "SELECT count(*) as num FROM q_event WHERE group_id = %s AND host_id = %s AND type = 'contentChange' and status =0", (group_id, host_id))
        contenthangeNum = str(contenthangeNum.get('num'))
        # 仿冒网站数
        fishNum = self.db.getOne(
            "SELECT count(*) as num FROM q_event WHERE group_id = %s AND host_id = %s AND type = 'fish' and status =0", (group_id, host_id))
        fishNum = str(fishNum.get('num'))
        # 违规内容数
        tamperNum = self.db.getOne(
            "SELECT count(*) as num FROM q_event WHERE group_id = %s AND host_id = %s AND (type = 'word' OR type = 'tamper') and status =0", (group_id, host_id))
        tamperNum = str(tamperNum.get('num'))
        # 未知资产数
        hostNum = self.db.getOne(
            "SELECT host_num FROM q_host_user where group_id=%s AND host_id=%s", (group_id, host_id))
        hostNum = str(hostNum.get('host_num'))
        # 可用性事件数
        monitorNum = self.db.getOne(
            "SELECT count(*) as num FROM q_event WHERE group_id = %s AND host_id = %s AND type = 'monitor' and status =0", (group_id, host_id))
        monitorNum = str(monitorNum.get('num'))
        return [scanNum, vulnewsNum, contenthangeNum, fishNum, tamperNum, hostNum, monitorNum]
