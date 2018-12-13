from classes import Job
from parser_ import parse_system
import matplotlib.pyplot as plt
from matplotlib import collections  as mc

def simulate_edf(args):
    """Runs a scheduling simulation using EDF priority scheduler."""
    params = vars(args)
    tasks = parse_system(params["input_file"])
    scheduler = EdfScheduler()
    simulate(scheduler, tasks, params["start"], params["stop"])

def simulate_llf(args):
    """Runs a scheduling simulation using LLF priority scheduler."""
    params = vars(args)
    tasks = parse_system(params["input_file"])
    scheduler = LlfScheduler()
    simulate(scheduler, tasks, params["start"], params["stop"])

def simulate(scheduler, tasks, start, stop):
    """Runs a scheduling simulation with a given scheduler, a set of tasks and
    the start and stop time. The simulation in fact will be conducted from
    t = zero to stop, but the log will be printed only after t = start.
    """
    print("Schedule from:", start, "to:", stop, ";", len(tasks), "tasks")
    jobs = []
    preemption_count = 0
    # The job currently scheduled
    current = None
    # The time since the current job has been lastly started
    # It is used only for printing
    uptime_current = 0
    # Lists tracing execution events for plotting
    executions = []
    releases = []
    for t in range(stop + 1):
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
                if t >= start:
                    releases.append((t, new_job.task.index))
        job_arrivals.sort(key = lambda job : job.task.index)

        # Sort the jobs by priority
        scheduler.sort_jobs(jobs)
        # Take the jobs with highest priority
        scheduled = jobs[0] if len(jobs) > 0 else None
        # If the scheduled job is a different one
        if scheduled != current and current != None:
            if t - uptime_current >= start:
                print(t - uptime_current, "-", t, ": ", current)
                executions.append([(t - uptime_current, current.task.index), (t, current.task.index)])
                # If we do a preemption, increment the counter
                if current.remaining_execution_time > 0 and current not in deadline_misses:
                    preemption_count += 1
            uptime_current = 0

        # Schedule the job
        current = scheduled

        if t >= start:
            # Print the log
            for deadline_miss in deadline_misses:
                print(t, ": Job ", deadline_miss, " misses a deadline", sep="")
            for job_arrival in job_arrivals:
                print(t, ": Arrival of job ", job_arrival, sep="")

    print("END: {0} preemptions".format(preemption_count))
    visualizeSimulation(executions, releases, start, stop, len(tasks), scheduler.name())

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


def visualizeSimulation(lines, releases, start, stop, n_task, scheduler_name):
    """Plots the given scheduling events.
    Params:
        lines: The lines indicating the scheduled jobs
        releases: The job release events
        start: the start time
        stop: the stop time
        n_tasks: the number of tasks
        scheduler_name: the name of the scheduler, used in the title of the plot.
    """
    fig2, ax2 = plt.subplots(figsize=(9, 5))
    lc = mc.LineCollection(lines, linewidths=10)
    ax2.add_collection(lc)
    ax2.autoscale()
    # Plot release arrows
    release_arrow_length = 0.5
    for release in releases:
        plt.arrow(release[0], release[1] + release_arrow_length, 0, -release_arrow_length,
            width=0.08, head_width=0.2, head_length=0.1, length_includes_head=True,
            facecolor="black", edgecolor="none")
    # Set up axes
    plt.grid(linestyle='dotted')
    plt.xlim([start - 1, stop + 1])
    plt.ylim([-1, n_task])
    plt.ylabel("Task index")
    plt.xlabel("Time t")
    plt.yticks(list(range(n_task)))
    plt.xticks(list(range(start - 1, stop + 1)))
    plt.title("Simulation done by the {0}-scheduler".format(scheduler_name))
    plt.show()
