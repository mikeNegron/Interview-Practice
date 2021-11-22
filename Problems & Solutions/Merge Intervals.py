'''
Problem:
Given an array of intervals where intervals[i] = [starti, endi]
merge all overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.
'''

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()
    results = []
        
    for i in intervals:
        if not results or results[-1][1] < i[0]:
            results.append(i)
                
        results[-1][1] = max(results[-1][1], i[1])        
    return results

def main():
    #Output should be [[1,6],[8,10],[15,18]]
    test = [[1,3],[2,6],[8,10],[15,18]]

    result = merge_intervals(test)

    print(f'The non-overlapping intervals are: {result}')

if __name__ == '__main__':
    main()