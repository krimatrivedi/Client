from django.db import models

class Book(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPES = (
        (HARDCOVER, 'Hardcover'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'E-book'),
    )
    clientname = models.CharField(max_length=50)
    clientcompany = models.CharField(max_length=50,null=True)
    clientphone = models.CharField(max_length=30, blank=True)
    clientemail = models.CharField(max_length=50)
    
    
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    def __str__(self):
        return self.clientname

CLI_TYPES=(
        ('client01','client01'),
        ('client02','client02'),
        ('client03','client03')
    )
DEP_TYPES = (
        ('DevelopmentDepartment', 'DevelopmentDepartment'),
        ('ManagersDepartment', 'ManagersDepartment'),
        ('ApplicationDepartment', 'ApplicationDepartment'),
        ('AccountsDepartments','AccountsDepartments')
    )
PRIO_TYPES=(
        ('High','High'),
        ('Medium','Medium'),
        ('Low','Low')
    )
STATUS_SELECT = (
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
        ('OnProgress', 'OnProgress')
    )
class Project(models.Model):

    projectid = models.CharField(max_length=50)
    projectname = models.CharField(max_length=50,null=True)
    Department = models.CharField(max_length=50,choices=DEP_TYPES)
    priority = models.CharField(max_length=50,choices=PRIO_TYPES)
    client = models.ForeignKey(Book, on_delete=models.PROTECT)
    workstatus = models.CharField(max_length=11,choices=STATUS_SELECT,null=True,default='Pending')
    timestamp = models.DateField(auto_now_add=True, auto_now=False),
    
