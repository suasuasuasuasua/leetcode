from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # there are a total of numCourses that i must take (0 --> numCourses - 1)
        #
        # prerequisites[i] = [a_i, b_i] where b_i is a dependency of a_i
        # course -> list of dependents
        # dependents -> list of courses that will "unlock"
        seen = defaultdict(set)
        deps = defaultdict(set)

        # build the adjacency lists
        for course, prereq in prerequisites:
            seen[course].add(prereq)
            deps[prereq].add(course)

        # formally known as Kahn's algorithm -- BFS based topological sort
        # get all courses without any dependents
        # this counts courses that are not dependents on any other courses
        no_deps = [i for i in range(numCourses) if len(seen[i]) == 0]
        taken = 0
        queue = deque(no_deps)
        while queue:
            # course is a dependency of others
            course = queue.popleft()
            taken += 1 # a course is taken once it is popped from the queue
            # use the reverse mapping to connect the dependency back to dependents
            for dep in deps[course]:
                seen[dep].remove(course)
                # count in-degrees -- if no more dependencies, then it is ready
                if len(seen[dep]) == 0:
                    queue.append(dep)

        return numCourses == taken
