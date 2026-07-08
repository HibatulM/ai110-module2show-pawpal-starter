"""PawPal system class skeletons generated from diagrams/uml.mmd."""

from datetime import datetime, time


class Pet:
    def __init__(
        self,
        id: str,
        name: str,
        animal_type: str,
        age: int,
        breed: str,
        vet: str,
        dietary_restrictions: list[str] | None = None,
        medications: list[str] | None = None,
        owner: "Owner | None" = None,
        tasks: list["Task"] | None = None,
    ):
        self.id = id
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.breed = breed
        self.vet = vet
        self.dietary_restrictions = dietary_restrictions or []
        self.medications = medications or []
        self.owner = owner
        self.tasks = tasks or []

    def get_pet_info(self) -> str:
        pass

    def get_task_list(self) -> list["Task"]:
        return self.tasks

    def add_task(self, task: "Task") -> None:
        """Add a task to this pet's list; called by the owner when a task is created."""
        pass

    def remove_task(self, task: "Task") -> None:
        """Remove a task from this pet's list; called by the owner."""
        pass


class Owner:
    def __init__(
        self,
        schedule: "Schedule | None" = None,
        pet_list: list[Pet] | None = None,
        tasks_list: list["Task"] | None = None,
        preferences: dict | None = None,
    ):
        self.schedule = schedule
        self.pet_list = pet_list or []
        self.tasks_list = tasks_list or []
        self.preferences = preferences or {}

    @property
    def number_of_pets(self) -> int:
        return len(self.pet_list)

    @property
    def number_of_tasks(self) -> int:
        return len(self.tasks_list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet and set its owner back-reference to self."""
        pass

    def remove_pet(self, pet: Pet) -> None:
        pass

    def add_task(self, task: "Task") -> None:
        """Create a task: append to the owner's list and call task.pet.add_task to update that pet's list."""
        pass

    def remove_task(self, task: "Task") -> None:
        """Remove a task from the owner's list and call task.pet.remove_task to update that pet's list."""
        pass

    def get_all_tasks(self) -> list["Task"]:
        """Return every task across all of the owner's pets."""
        return self.tasks_list

    def get_tasks_for_pet(self, pet: Pet) -> list["Task"]:
        """Return the tasks belonging to a single pet."""
        pass

    def get_schedule(self) -> "Schedule":
        pass

    def generate_schedule_for_all_pets(self) -> "Schedule":
        pass

    def generate_schedule_for_one_pet(self, pet: Pet) -> "Schedule":
        pass

    def add_preference(self, key: str, value: str) -> None:
        pass

    def remove_preference(self, key: str) -> None:
        pass


class Task:
    def __init__(
        self,
        id: str,
        pet: Pet,
        description: str,
        scheduled_time: datetime | None = None,
        frequency: str = "once",
        priority: int = 0,
        location: str = "",
        duration: int = 0,
        completed_time: datetime | None = None,
    ):
        self.id = id
        self.pet = pet
        self.description = description
        # When the activity happens.
        self.scheduled_time = scheduled_time
        # How often it repeats, e.g. "once", "daily", "weekly".
        self.frequency = frequency
        self.priority = priority
        self.location = location
        self.duration = duration
        # When it was completed; None until done.
        self.completed_time = completed_time

    @property
    def task_completed(self) -> bool:
        return self.completed_time is not None

    @property
    def repeat_task(self) -> bool:
        return self.frequency != "once"

    def mark_completed(self, completed_time: datetime) -> None:
        pass

    def change_priority(self, priority: int) -> None:
        pass


class Schedule:
    def __init__(
        self,
        owner: "Owner | None" = None,
        days_of_week: list[str] | None = None,
        work_start: time = time(8, 0),
        work_end: time = time(20, 0),
        blocked_times: list[tuple[datetime, datetime]] | None = None,
    ):
        self.owner = owner
        self.days_of_week = days_of_week or []
        # Working window tasks are placed within (default 8am-8pm).
        self.work_start = work_start
        self.work_end = work_end
        # (start, end) intervals already taken; starts empty (no time blocked).
        self.blocked_times = blocked_times or []

    @property
    def tasks(self) -> list[Task]:
        """The scheduler reads the owner's single task list."""
        return self.owner.tasks_list if self.owner else []

    def is_time_free(self, start: datetime, end: datetime) -> bool:
        """True if [start, end) sits in working hours and overlaps no blocked interval."""
        pass

    def find_free_slot(self, duration: int, after: datetime | None = None) -> datetime | None:
        """Find the earliest working-hours slot of `duration` that is not blocked."""
        pass

    def block_time_for_task(self, task: Task) -> None:
        """Reserve the task's scheduled_time (or the next free 8am-8pm slot) and record the block."""
        pass

    def block_time_for_repeated_task(self, task: Task) -> None:
        pass

    def reschedule_tasks(self) -> None:
        """Re-place tasks by priority within working hours, respecting blocked intervals."""
        pass

    def get_upcoming_tasks_for_day(self, pet: Pet | None = None) -> list[Task]:
        """Upcoming tasks for the day; if pet is given, limit to that pet's tasks."""
        pass

    def get_upcoming_tasks_for_week(self, pet: Pet | None = None) -> list[Task]:
        """Upcoming tasks for the week; if pet is given, limit to that pet's tasks."""
        pass

    def get_upcoming_tasks_for_month(self, pet: Pet | None = None) -> list[Task]:
        """Upcoming tasks for the month; if pet is given, limit to that pet's tasks."""
        pass

    def change_time_for_repeated_task_once(self, task: Task, time: datetime) -> None:
        pass

    def change_time_for_task(self, task: Task, time: datetime) -> None:
        pass
