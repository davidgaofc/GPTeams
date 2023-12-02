import timeit
import datetime
from radon.complexity import cc_visit
import inspect
import extracted_out.question6.n1 as n1
import extracted_out.question6.n2 as n2
import extracted_out.question6.n3 as n3
# Import the necessary modules and classes here
# from your_module import Patient, Doctor, Appointment, cancel_appointment

# Sample test cases for cancel_appointment function
test_cases = [
    # Case 1: Single appointment in the list
    (n1.Doctor("Dr. Smith", "Cardiology"), n1.Patient("John Doe", 30, "Healthy"), [datetime.datetime.now()+datetime.timedelta(days=1)]),

    # Case 2: Multiple appointments, cancel the first
    (n1.Doctor("Dr. Jones", "Neurology"), n1.Patient("Alice Johnson", 40, "Migraine"),
     [datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=1)]),

    # Case 3: Multiple appointments, cancel the middle one
    (n1.Doctor("Dr. Brown", "Dermatology"), n1.Patient("Bob Brown", 50, "Eczema"),
     [datetime.datetime.now() + datetime.timedelta(days=1), datetime.datetime.now() + datetime.timedelta(days=2), datetime.datetime.now() + datetime.timedelta(days=3)]),

    # Case 4: Multiple appointments, cancel the last one
    (n1.Doctor("Dr. White", "Pediatrics"), n1.Patient("Eve White", 10, "Flu"),
     [datetime.datetime.now() + datetime.timedelta(days=1), datetime.datetime.now() + datetime.timedelta(days=2), datetime.datetime.now()+datetime.timedelta(days=3)]),

    # Case 5: Cancel an appointment from a fully booked doctor
    (n1.Doctor("Dr. Green", "Orthopedics"), n1.Patient("Gary Green", 60, "Arthritis"),
     [datetime.datetime.now() + datetime.timedelta(days=i) for i in range(5)]),

    # Case 6: Cancel an appointment where patient has appointments with multiple doctors
    (n1.Doctor("Dr. Grey", "General"), n1.Patient("Hannah Grey", 35, "Checkup"),
     [datetime.datetime.now() + datetime.timedelta(days=2), datetime.datetime.now() + datetime.timedelta(days=4)]),

    # Case 7: Cancel the only appointment of a new patient
    (n1.Doctor("Dr. Black", "Oncology"), n1.Patient("Ivy Black", 45, "Consultation"),
     [datetime.datetime.now() + datetime.timedelta(days=3)]),

    # Case 8: Patient with a past and future appointment, cancel the future one
    (n1.Doctor("Dr. Purple", "Gastroenterology"), n1.Patient("Jack Purple", 55, "Gastritis"),
     [datetime.datetime.now() - datetime.timedelta(days=3), datetime.datetime.now() + datetime.timedelta(days=3)]),

    # Case 9: Patient with back-to-back appointments, cancel the second one
    (n1.Doctor("Dr. Yellow", "Cardiology"), n1.Patient("Kathy Yellow", 65, "Heart Checkup"),
     [datetime.datetime.now()+ datetime.timedelta(minutes=15), datetime.datetime.now() + datetime.timedelta(minutes=30)]),

    # Case 10: Complex case - multiple patients, same doctor, cancel one appointment for each patient
    (n1.Doctor("Dr. Azure", "Neurology"),
     [n1.Patient("Larry Azure", 75, "Neurological Exam"), n1.Patient("Molly Azure", 25, "Headache")],
     [datetime.datetime.now()+ datetime.timedelta(days=1), datetime.datetime.now() + datetime.timedelta(days=2)])
]


def setup_test_case(doctor, patients, dates):
    if not isinstance(patients, list):
        patients = [patients]

    appointments = []
    for patient in patients:
        for date in dates:
            appointment = n1.Appointment(patient, doctor, date)
            patient.schedule_appointment(date, doctor)
            appointments.append(appointment)

    return appointments

def test_cancel_appointment_functionality(cancel_appointment_func):
    correct_count = 0
    for doctor, patient, dates in test_cases:
        try:
            appointments = setup_test_case(doctor, patient, dates)
            initial_count_d = len(n1.get_doctor_appointments(doctor))
            initial_count_p = len(n1.list_patient_appointments(patient))
            cancel_appointment_func(appointments[0])
            final_count_d = len(n1.get_doctor_appointments(doctor))
            final_count_p = len(n1.list_patient_appointments(patient))
            if final_count_d == initial_count_d - 1 and final_count_p == initial_count_p - 1:
                correct_count += 1
        except:
            # print("exception")
            pass
    return correct_count

def calculate_complexity(func):
    source_code = inspect.getsource(func)
    complexity_result = cc_visit(source_code)
    for item in complexity_result:
        if item.name == func.__name__:
            return item.complexity
    return None

def test_performance(cancel_appointment_func):
    times = []
    for doctor, patient, dates in test_cases:
        try:
            appointments = setup_test_case(doctor, patient, dates)
            time_taken = timeit.timeit(lambda: cancel_appointment_func(appointments[0]), number=100)
            times.append(time_taken)
        except:
            pass
    if(len(times) == 0):
        return None
    return sum(times) / len(times)

def write_results_to_file(filename, n, functional_results, complexity, performance_results):
    with open(filename, 'w') as file:
        file.write(f"Results for solution {n}:\n")
        file.write("Functional Test Results: " + str(functional_results) + '\n')
        file.write("Cyclomatic Complexity: " + str(complexity) + '\n')
        file.write("Performance Test Results: " + str(performance_results) + '\n')

def main():
    for n, module in enumerate([n1, n2, n3], 1):
        cancel_appointment_func = module.cancel_appointment  # Replace with your function reference
        functional_results = test_cancel_appointment_functionality(cancel_appointment_func)
        complexity = calculate_complexity(cancel_appointment_func)
        performance_results = test_performance(cancel_appointment_func)
        write_results_to_file(f'../test_results/q6-{n}.txt', n, functional_results, complexity, performance_results)

main()