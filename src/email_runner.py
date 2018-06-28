import pandas as pd
import requests


def send_simple_message(template, email, name, apiKey, subject, domain, domainKey):
    '''
    @param template - email template you want to send fill template where name and username is with {}
    @param email - email address you want the email to be sent to, can be a list or can be contained in excel file
    @param name - name of the person who is receiving 
    @param apiKey - your mailgun API Key
    @param subject - the subject of the email
    @param domain - your mailgun domain
    @output sends out emails
    '''
    return requests.post(
        "https://api.mailgun.net/v3/"+ domainKey +".mailgun.org/messages",
        auth=("api", apiKey),
        data={"from": "Mailgun Sandbox <" + domain + ".mailgun.org>",
              "to": "" + name +  "<" + email + ">",
              "subject": subject,
              "text": template})



'''
@param: excel file
@param: sheet#
@param: usecols = column numbers you want to use
@output: pandas dataframe that reads the excel file
'''
df = pd.read_excel("", 'Sheet1', index_col=None, na_values=['NA'],usecols=[1,2,6,7,8])



template = """   """   ## email template
email = [""]           ## email
name = [""]            ## name
apiKey = ""            ## API Key
subject = ""           ## subject
domain = ""            ## domain
domainKey = ""         ## domainKey

for row in df.itertuples():
    '''Sends emails for all rows in excel file
    format should contain arguemtns you want placed in tempalte'''
    send_simple_message(template.format(),email,name,apiKey,subject,domain,domainKey)
    print("sent {} emails".format(row[0] + 1))
    