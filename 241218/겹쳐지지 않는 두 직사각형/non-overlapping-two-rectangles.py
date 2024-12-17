n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))


def find_all_possible_rectangles(n: int, m: int) -> list[tuple]:
    rectangles = [] # (topleft_i, topleft_j, bottomright_i, bottomright_j)
    for topleft_i in range(n):
        for topleft_j in range(m):
            for bottomright_i in range(topleft_i, n):
                for bottomright_j in range(topleft_j, m):
                    rectangles.append( (topleft_i, topleft_j, bottomright_i, bottomright_j) )
    return rectangles


def all_coordinates_in(rectangle: list[tuple]) -> set[tuple]:
    topleft_i, topleft_j, bottomright_i, bottomright_j = rectangle
    coordinates = set()
    for i in range(topleft_i, bottomright_i + 1):
        for j in range(topleft_j, bottomright_j + 1):
            coordinates.add( (i, j) )
    return coordinates


def is_overlapped(first_rectangle, second_rectangle):
    if all_coordinates_in(first_rectangle) & all_coordinates_in(second_rectangle):
        return True
    return False


def find_second_rectangles(n: int, m: int, first_rectangle: list[tuple]) -> list[tuple]:
    res = []
    candidates = find_all_possible_rectangles(n, m)
    for second_rectangle in candidates:
        if not is_overlapped(first_rectangle, second_rectangle):
            res.append(second_rectangle)
    return res


def sum_in(rectangle, mat):
    topleft_i, topleft_j, bottomright_i, bottomright_j = rectangle
    res = 0
    for i, j in all_coordinates_in(rectangle):
        res += mat[i][j]
    return res


def solution(n, m, mat):
    ans = -1e9
    first_rectangles = find_all_possible_rectangles(n, m)
    for first_rectangle in first_rectangles:
        second_rectangles = find_second_rectangles(n, m, first_rectangle)
        for second_rectangle in second_rectangles:
            ans = max( ans, sum_in(first_rectangle, mat) + sum_in(second_rectangle, mat) )
    return ans

print(solution(n, m, mat))

