"""PawPal system class skeletons generated from diagrams/uml.mmd."""

from datetime import datetime


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
        self.tasks = tasks or []

    def get_pet_info(self) -> str:
        pass

    def get_task_list(self) -> list["Task"]:
        pass

    def add_task(self, task: "Task") -> None:
        pass

    def remove_task(self, task: "Task") -> None:
        pass


class Owner:
    def __init__(
        self,
        number_of_pets: int = 0,
        number_of_tasks: int = 0,
        schedule: "Schedule | None" = None,
        pet_list: list[Pet] | None = None,
        tasks_list: list["Task"] | None = None,
        preferences: dict | None = None,
    ):
        self.number_of_pets = number_of_pets
        self.number_of_tasks = number_of_tasks
        self.schedule = schedule
        self.pet_list = pet_list or []
        self.tasks_list = tasks_list or []
        self.preferences = preferences or {}

    def add_pet(self, pet: Pet) -> None:
        pass

    def remove_pet(self, pet: Pet) -> None:
        pass

    def get_schedule(self) -> "Schedule":
        pass

    def generate_schedule_for_all_pets(self) -> "Schedule":
        pass

    def generate_schedule_for_one_pet(self, pet: Pet) -> "Schedule":
        pass

    def add_time_constraints(self, constraint: "TimeConstraint") -> None:
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
        repeat_task: bool = False,
        task_completed: bool = False,
        priority: int = 0,
        location: str = "",
        duration: int = 0,
        scheduled_time: datetime | None = None,
    ):
        self.id = id
        self.pet = pet
        self.description = description
        self.repeat_task = repeat_task
        self.task_completed = task_completed
        self.priority = priority
        self.location = location
        self.duration = duration
        self.scheduled_time = scheduled_time

    def add_task(self, task: "Task") -> None:
        pass

    def remove_task(self, task: "Task") -> None:
        pass

    def mark_completed(self) -> None:
        pass

    def change_priority(self, priority: int) -> None:
        pass


class Schedule:
    def __init__(
        self,
        days_of_week: list[str] | None = None,
        time_blocked: list["TimeBlock"] | None = None,
        time_free: list["TimeBlock"] | None = None,
        tasks_to_schedule: list[Task] | None = None,
    ):
        self.days_of_week = days_of_week or []
        self.time_blocked = time_blocked or []
        self.time_free = time_free or []
        self.tasks_to_schedule = tasks_to_schedule or []

    def add_free_time(self, block: "TimeBlock") -> None:
        pass

    def block_time_for_task(self, task: Task) -> None:
        pass

    def block_time_for_repeated_task(self, task: Task) -> None:
        pass

    def add_busy_time(self, block: "TimeBlock") -> None:
        pass

    def reschedule_tasks(self) -> None:
        pass

    def get_upcoming_tasks_for_day(self) -> list[Task]:
        pass

    def get_upcoming_tasks_for_week(self) -> list[Task]:
        pass

    def get_upcoming_tasks_for_month(self) -> list[Task]:
        pass

    def change_time_for_repeated_task_once(self, task: Task, time: datetime) -> None:
        pass

    def change_time_for_task(self, task: Task, time: datetime) -> None:
        pass
