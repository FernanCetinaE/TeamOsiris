from pylovepdf.ilovepdf import ILovePdf

ilovepdf = ILovePdf(
    "project_public_1ed8cbf7ceb806075f868bc7ff18aeb3_VMWJR9477e2776bb332c4b14fc072c70919a7",
    verify_ssl=True,
)

task = ilovepdf.new_task("compress")
task.add_file("test.pdf")
task.set_output_folder("./")
task.execute()
task.download()
task.delete_current_task()