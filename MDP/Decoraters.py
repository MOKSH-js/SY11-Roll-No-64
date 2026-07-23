def format_report(func):
    def wrapper(*args,**kwargs):
        print("\n"+"="*40)
        print(*args,**kwargs)
        print("="*40)
    return wrapper

class Report:
    templates={}

    def __init__(self,title,content,template):
        self.title=title
        self.content=content
        self.template=template

    @classmethod
    def add_template(cls,name,description):
        cls.templates[name]=description
    def __str__(self):
        return(
            f"Title :{self.title}\n"
            f"Content :{self.content}\n"
            f"template :{self.template}\n"
        )
    @format_report
    def generate_report(self):
        print(self)
Report.add_template("Bussiness","Business Report Template")
Report.add_template("Acadeemic","Acadeemic Report Template")
report=Report(
    "Monthly Sales",
    "Sales increased by 20% this month",
    "business"
)
report.generate_report()