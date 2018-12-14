class Task:
    def __init__(self, offset, wcet, period, index):
        self.offset = offset
        self.wcet = wcet
        self.period = period
        self.index = index
        self.job_counter = 0


class Job:
    def __init__(self, task):
        self.task = task
        self.remaining_execution_time = task.wcet
        self.time_to_deadline = task.period
        self.name = "T" + str(task.index) + "J" + str(task.job_counter)
        task.job_counter += 1

    def __str__(self):
        return self.name
