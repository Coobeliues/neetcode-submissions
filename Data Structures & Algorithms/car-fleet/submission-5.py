class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # cars = sorted(zip(position, speed), reverse = True)

        # cars = [(p, s) for p, s in zip(position, speed)]
        # cars.sort(reverse=True)

        cars = sorted([(p, (target - p) / s) for p, s in zip(position, speed)], reverse=True)
        stack = []

        for p, time in cars:
            # time = (target - p) / s

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)