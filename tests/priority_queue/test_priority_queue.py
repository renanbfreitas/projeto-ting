import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    priorityQI = PriorityQueue()
    priorityQI.enqueue({"qtd_linhas": 9})
    priorityQI.enqueue({"qtd_linhas": 4})
    priorityQI.enqueue({"qtd_linhas": 2})
    priorityQI.enqueue({"qtd_linhas": 5})
    priorityQI.enqueue({"qtd_linhas": 7})
    priorityQI.enqueue({"qtd_linhas": 11})
    priorityQI.enqueue({"qtd_linhas": 3})

    assert len(priorityQI) == 7
    with pytest.raises(IndexError):
        priorityQI.search(10)
    assert priorityQI.dequeue() == {"qtd_linhas": 4}
    assert priorityQI.search(0) == {"qtd_linhas": 2}
