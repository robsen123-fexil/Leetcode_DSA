"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employes_id={emp.id: emp for emp in employees}
        print(list(employes_id))
        total=0
        que=deque([id])
        while que:
            currid=que.popleft()
            empl=employes_id[currid]
            total+=empl.importance
            que.extend(empl.subordinates)
        return total
