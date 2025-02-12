class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        l=0
        count=0
        print(seats , students)
        while l<len(seats):
            count+=(abs(seats[l]-students[l]))
            l+=1
        return count

