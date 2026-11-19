class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        cnt = 0
        lead_time = 0

        for pos, s in cars:
            curr_time = (target - pos) / s

            if curr_time > lead_time:
                cnt += 1
                lead_time = curr_time
        
        return cnt 