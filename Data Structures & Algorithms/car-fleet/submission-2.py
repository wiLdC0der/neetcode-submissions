class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = []

        for i in range(len(position)):
            total = (target-position[i])/speed[i]
            cars.append([position[i],total])
        count = 0
        maximum = 0

        cars.sort(reverse = True)
        for k,v in cars:
            if v > maximum:
                count+=1
                maximum = v
        return count




        