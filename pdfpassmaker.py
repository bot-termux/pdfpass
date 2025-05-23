# github.com/bot-termux
import os
import pikepdf
import logging
import coloredlogs

# SET PASSWORD HERE
pdf_password = "yourpassword"

# Logs to scriptName.log
scriptName = os.path.basename(__file__)
logging.basicConfig(
    level=logging.DEBUG,
    filename=scriptName + ".log",
    filemode="a",
    encoding='utf-8',
    format='[%(asctime)s] [%(levelname)s] %(message)s'
)

# Logs into console
mylogs = logging.getLogger(__name__)
stream = logging.StreamHandler()
mylogs.addHandler(stream)
coloredlogs.install(
    level=logging.DEBUG,
    logger=mylogs,
    fmt='[%(asctime)s] [%(levelname)s] %(message)s'
)

rootdir = os.getcwd()
nb = 0

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = os.path.join(subdir, file)
        if filepath.endswith(".pdf"):
            nb += 1
            mylogs.info(f"{nb}) File processing : {file} ({filepath})")
            try:
                with pikepdf.open(filepath) as pdf:
                    new_filepath = filepath.replace(".pdf", "_locked.pdf")
                    pdf.save(new_filepath, encryption=pikepdf.Encryption(owner=pdf_password, user=pdf_password, R=4))
                    mylogs.info(f"Password added to {file} → saved as {os.path.basename(new_filepath)}")
            except Exception as e:
                mylogs.error(f"Failed to add password to {file}: {e}")

os.system("pause")

