from cmysql import insert_musk, insert_news, insert_jobs

class Mush(object):

    def __init__(self, ttime, ttype, tcontent):
        self.ttime = ttime
        self.ttype = ttype
        self.tcontent = tcontent


class News(object):

    def __init__(self, ntype, content, ntime, url, tokens=None):
        self.ntime = ntime
        self.ntype = ntype
        self.content = content
        self.url = url
        self.tokens = tokens


class Job(object):

    def __init__(self, jtype, content):
        self.jtype = jtype
        self.content = content


def analysis_musk(content=None):
    ''' example
    07:03:54
    [Tweet]

    **How to sabotage an organization … ****https://t.co/YWtfgfRKCu**
    '''
    content = content.strip()
    tweet_time = content.split('\n')[0]
    tweet_content = content[len(tweet_time):].strip()
    if tweet_content.startswith('[Tweet]'):
        ttype = '[Tweet]'
        content = tweet_content[len('[Tweet]'):].strip()
    elif tweet_content.startswith('[Reply]'):
        ttype = '[Reply]'
        content = tweet_content[len('[Reply]'):].strip()
    elif tweet_content.startswith('[ReTweet]'):
        ttype = '[Tweet]'
        content = tweet_content[len('[ReTweet]'):].strip()
    insert_musk(tweet_time, ttype, content)


def analysis_news(content=None):
    ''' example
    [PYR官方推特 @VulcanForged]

    **Let's celebrate the ****@VulcanStudiosHQ** **rebrand with a ****#giveaway****! 🎉

    For a chance to win:
    ✅ Follow ****@VulcanStudiosHQ**
    **💚 Like & RT ****@VulcanStudiosHQ****'s pinned Tweet

    10,000 XP and 100 ****$PYR** **to one random mortal who completes all the steps.

    You've got 96 hours

    Best of luck!**
    $BTC、$NFT
    ————————————
    发布时间：2023-03-05 15:45:00
    链接：https://twitter.com/VulcanForged/status/1632286071496101891
    '''
    content = content.strip()
    if content.find('译文') == -1:
        print('This content does not contains Translation, so skip it.')
        return
    ntype = content.split('\n')[0]
    ntype_num = 0
    if ntype.find('币安') > -1:
        ntype_num = 1
    elif ntype.find('博客') > -1:
        ntype_num = 2
    elif ntype.find('新闻') > -1 or ntype.find('快讯') > -1:
        ntype_num = 3
    elif ntype.find('上新') > -1:
        ntype_num = 4
    news_content = content[len(ntype):].strip()
    url = news_content.split('链接：')[-1]
    news_content = news_content[:len(news_content)-len('链接：'+url)].strip()
    ntime = news_content.split('发布时间：')[-1]
    news_content = news_content[:len(news_content) - len('发布时间：' + ntime)].strip()
    lines = news_content.split('\n')[-1].strip()
    news_content = news_content.replace(lines, '').strip()
    tokens = news_content.split('\n')[-1].strip()
    if not url or not news_content:
        insert_news('', '', content, '', '', ntype_num)
        return

    if tokens.find('$') > -1:
        news_content = news_content.replace(tokens, '').strip()
        insert_news(ntime, ntype, news_content, url, tokens, ntype_num)
    else:
        tokens = ''
        insert_news(ntime, ntype, news_content, url, '', ntype_num)
    


def analysis_job(content=None):
    ''' example
    #招聘 
    KuCoin - 交易所
    https://www.kucoin.com/
    
    #兼职 #实习
    去中心化NFT市场运营
    
    1、协助制定NFT聚合交易平台运营方案
    2、根据产品定位对同类竞品完成市场调研报告，并输出建议
    3、NFT社群管理
    
    要求：
    1、有NFT相关运营经验，有过NFT聚合平台运营经验优先
    2、会使用Gleam、Quest3等用户增长工具
    3、英文能作为工作语言
    
    ✅远程 #global 
    
    投递
    Telegram：@KK20302030
    '''
    content = content.strip()
    jtype = content.split('\n')[0].strip()
    jcontent = content.replace(jtype, '').strip()
    print(jtype)
    if jtype == '#招聘':
        insert_jobs(jtype, jcontent)
    elif jtype == '#求职':
        insert_jobs(jtype, jcontent)
    else:
        print('error')


