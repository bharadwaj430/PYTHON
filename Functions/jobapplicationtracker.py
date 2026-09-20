# AI Job Application Tracker

applications = []


# 1. Add a new job application
def add_application(company, role, status):
    application = {
        "company": company,
        "role": role,
        "status": status
    }

    applications.append(application)
    print("Application added successfully!")


# 2. Display all applications
def show_applications():
    print("\n===== MY APPLICATIONS =====")

    if len(applications) == 0:
        print("No applications found.")
        return

    for i, application in enumerate(applications, start=1):
        print(
            i,
            application["company"],
            "-",
            application["role"],
            "-",
            application["status"]
        )


# 3. Count applications by status
def count_status(status):
    count = 0

    for application in applications:
        if application["status"] == status:
            count += 1

    return count


# 4. Calculate application statistics
def show_statistics():
    total = len(applications)
    applied = count_status("Applied")
    interview = count_status("Interview")
    rejected = count_status("Rejected")
    selected = count_status("Selected")

    print("\n===== APPLICATION STATISTICS =====")
    print("Total Applications :", total)
    print("Applied            :", applied)
    print("Interviews         :", interview)
    print("Rejected           :", rejected)
    print("Selected           :", selected)


# 5. Find applications requiring follow-up
def follow_up():
    print("\n===== FOLLOW-UP REQUIRED =====")

    for application in applications:

        if application["status"] == "Applied":
            print(
                application["company"],
                "-",
                application["role"]
            )


# Main program

add_application("Google", "AI/ML Intern", "Applied")
add_application("Microsoft", "Software Engineer Intern", "Interview")
add_application("TCS", "Python Developer", "Rejected")
add_application("Qualcomm", "AI Engineer Intern", "Applied")
add_application("Amazon", "ML Engineer Intern", "Selected")

show_applications()

show_statistics()

follow_up()