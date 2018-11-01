from classes import Job

def simulate(scheduler, tasks, start, stop):
    jobs = []
    preemption_count = 0
    # The job currently scheduled
    current = None
    # The time since the current job has been lastly started
    # It is used only for printing
    uptime_current = 0
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
        # If we do a preemption, increment the counter
        if scheduled != current and current != None:
            preemption_count += 1
            print(t - uptime_current, "-", t, ": ", current)
            uptime_current = 0
        # Schedule the job
        current = scheduled

        # Print the log
        for deadline_miss in deadline_misses:
            print(t, ": Job ", deadline_miss, " misses a deadline", sep="")
        for job_arrival in job_arrivals:
            print(t, ": Arrival of job ", job_arrival, sep="")

class EdfScheduler:
    def sort_jobs(self, jobs):
        jobs.sort(key = lambda job: job.time_to_deadline)
