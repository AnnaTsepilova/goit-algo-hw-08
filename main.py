import heapq


def min_cost_to_connect_cables(cables):
    # Якщо тільки один кабель, немає витрат на з'єднання
    if len(cables) == 1:
        return 0

    # Створюємо мінімальну купу
    heapq.heapify(cables)
    total_cost = 0

    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Витягуємо два найменших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Витрати на з'єднання
        cost = first + second
        total_cost += cost

        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost


# Приклад використання
cables = [8, 4, 6, 12]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))


# Необов'язкове завдання
def merge_k_lists(lists):
    # Мінімальна купа
    min_heap = []

    # Додаємо перші елементи кожного списку в купу
    for i, lst in enumerate(lists):
        if lst:  # Перевіряємо, що список не порожній
            heapq.heappush(min_heap, (lst[0], i, 0))

    result = []

    while min_heap:
        # Витягуємо мінімальний елемент
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)

        # Додаємо наступний елемент з того ж списку, якщо він існує
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))

    return result


# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)