from classes import Job
from parser_ import parse_system
import matplotlib.pyplot as plt
from matplotlib import collections  as mc

def simulate_edf(args):
    params = vars(args)
    tasks = parse_system(params["input_file"])
    scheduler = EdfScheduler()
    simulate(scheduler, tasks, params["start"], params["stop"])

def simulate_llf(args):
    params = vars(args)
    tasks = parse_system(params["input_file"])
    scheduler = LlfScheduler()
    simulate(scheduler, tasks, params["start"], params["stop"])

def simulate(scheduler, tasks, start, stop):
    jobs = []
    preemption_count = 0
    # The job currently scheduled
    current = None
    # The time since the current job has been lastly started
    # It is used only for printing
    uptime_current = 0
    executions=[]
    for t in range(start, stop):
        deadline_misses = []
        job_arrivals = []

        if current != None:
            current.remaining_execution_time -= 1
            uptime_current += 1
            if current.remaining_execution_time <= 0:
                jobs.remove(current)

        # Decrease time to deadline of all jobs
        for job in jobs:
            job.time_to_deadline -= 1
            if job.time_to_deadline <= 0 and job.remaining_execution_time > 0:
                deadline_misses.append(job)
                # Abort the job at its deadline, according to statement
                jobs.remove(job)
        deadline_misses.sort(key = lambda job : job.task.index)

        # Add a new job if it's realase time for a task
        for task in tasks:
            if (t - task.offset) % task.period == 0:
                new_job = Job(task)
                job_arrivals.append(new_job)
                jobs.append(new_job)
        job_arrivals.sort(key = lambda job : job.task.index)

        # Sort the jobs by priority
        scheduler.sort_jobs(jobs)
        # Take the jobs with highest priority
        scheduled = jobs[0] if len(jobs) > 0 else None
        # If the scheduled job is a different one
        if scheduled != current and current != None:
            print(t - uptime_current, "-", t, ": ", current)
            executions.append([(t - uptime_current, current.task.index), (t, current.task.index)])
            uptime_current = 0
            # If we do a preemption, increment the counter
            if current.remaining_execution_time > 0:
                preemption_count += 1

        # Schedule the job
        current = scheduled

        # Print the log
        for deadline_miss in deadline_misses:
            print(t, ": Job ", deadline_miss, " misses a deadline", sep="")
        for job_arrival in job_arrivals:
            print(t, ": Arrival of job ", job_arrival, sep="")

    print("END: {0} preemptions".format(preemption_count))
    visualizeSimulation(executions, stop, len(tasks), scheduler.name())

class EdfScheduler:
    def name(self):
        return "EDF"
    def sort_jobs(self, jobs):
        jobs.sort(key = lambda job: (job.time_to_deadline, job.task.index))


class LlfScheduler:
    def name(self):
        return "LLF"
    def sort_jobs(self, jobs):
        jobs.sort(key = lambda job: (job.time_to_deadline-job.remaining_execution_time, job.task.index))


def visualizeSimulation(lines, t, n_task, scheduler_name):
    fig2, ax2 = plt.subplots(figsize=(9, 5))
    lc = mc.LineCollection(lines, linewidths=2)
    ax2.add_collection(lc)
    ax2.autoscale()
    plt.xlim([-1,t+1])
    plt.ylim([-1,n_task])
    plt.ylabel("Task index")
    plt.xlabel("Time t")
    plt.yticks([i for i in range(n_task)])
    plt.xticks([i for i in range(lines[-1][-1][0]+2)])
    plt.title("Simulation done by the {0}-scheduler".format(scheduler_name))
    plt.show()
