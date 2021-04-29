

############ HTML Report Configuration ######################

def pytest_html_report_title(report):
    report.title = "Tests Results Report"


def pytest_configure(config):
    config._metadata["Project"] = "Google Search Automation Project"
    config._metadata["Tester"] = "Lucia Vallejos"
