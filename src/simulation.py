

def simulate(scheduler, tasks, start, stop):
    jobs = []
    preemption_count = 0
    current = None
    for t in range(start, stop):
        deadline_misses = []
        job_arrivals = []

        if current != None:
            current.remaining_execution_time -= 1
            if current.remaining_execution_time <= 0:
                jobs.remove(job)

        # Decrease time to deadline of all jobs
        for job in jobs:
            job.time_to_deadline -= 1
            if job.time_to_deadline <= 0 and job.remaining_execution_time > 0:
                deadline_misses.append(job)
        deadline_misses.sort(key = lambda job : job.task.index)

        # Add a new job if it's realase time for a task
        for task in tasks:
            if t - task.offset % task.period == 0:
                new_job = Job(task)
                job_arrivals.append(task)
                jobs.append(new_job)
        job_arrivals.sort(key = lambda job : job.task.index)

        # Sort the jobs by priority
        scheduler.sort_jobs(jobs)
        # Take the jobs with highest priority
        scheduled = jobs[0] if len(jobs) > 0 else None
        # If we do a preemption, increment the counter
        if scheduled != current and scheduled != None:
            preemption_count += 1
        # Schedule the job
        current = scheduled

        # Print the log
        for deadline_miss in deadline_misses:
            print(t, ": Job ", deadline_miss + " misses a deadline", sep="")
        for job_arrival in job_arrivals:
            print(t, ": Arrival of job ", job_arrival, sep="")
        # TODO: print the whole scheduled execution at once rather than
        # one line per time unit
        print(t, "-", t + 1, ": ", current, sep="")
