import pdb

con_fact = None
IRules = None


def dfs(_pre_facts, _con_fact, _IRules):
    # TODO seperate con_fact, Eg: H => G|H or worse
    global con_fact
    global IRules
    pre_facts = _pre_facts
    con_fact = _con_fact
    IRules = _IRules

    ser_node = con_fact['fact']
    nodes = [{
        'fact': ser_node,
        'type': 'con'
        }]
    facts = pre_facts
    results = []
    while True:
        results_temp = results.copy()
        ser_node, nodes, facts, results = search_node(ser_node, nodes, facts, results)
        if not results or results_temp == results:
            return False
        elif result[-1]['fact'] is con_fact['fact']:
            return result


def search_node(ser_node, nodes, facts, results):
    """ Search nodes that related to ser_node in DFS, and test the nodes then store the result, if the nodes pass the test, return results instead of False.

    :param ser_node: target node, a Fact instance
    :param nodes:    store nodes which are related, a list of Fact instances
    :param facts:    source, a list
    :param results:   current results, a list
    """
    if not ser_node:
        return ser_node, nodes, facts, results

    for c_fact in facts:
        if c_fact['fact'] in nodes:
            # avoid duplicated related nodes
            continue
        fact = c_fact['fact']
        fact_type = c_fact['type']  # type could be 'input' or 'result'
        # set temp variable
        facts_buffer = facts.copy()
        ser_node_buffer = ser_node
        nodes_buffer = nodes.copy()
        results_buffer = result.copy()

        if ser_node.value == fact.value:
            # G == G, -G == G
            pass
        elif ser_node.value in fact.value:
            # G, G*H
            nodes_buffer.append({
                'fact': fact,
                'type': fact_type
                })  # store current fact
            if ser_node.value in fact.left_child.value:
                ser_node_buffer = fact.right_child
            else:
                ser_node_buffer = fact.left_child
        elif fact.value in ser_node.value:
            # G*H, G
            pass

        if ser_node != ser_node_buffer:
            # nodes update, search next node
            s, n, f, r = search_node(ser_node_buffer, nodes_buffer, facts_buffer, results_buffer)
            if r != results:
                return s, n, f, r

    return test_node(nodes, facts, results)


def test():
    return


def test_node(nodes, facts, results):
    # return ser_node, nodes, facts, result
    if len(nodes) == 1:
        return None, nodes, facts, results

    nodes.reverse()
    cur_node = nodes[0]
    next_node = nodes[1]
    # 1 premise
    if cur_node['fact'] is con_fact['fact']:
        if cur_node['type'] == 'input':
            rule = 'P'
        elif cur_node['type'] == 'result':
            rule = cur_node['line']  # TODO
        result.append({
            'fact': cur_node['fact'],
            'rule': 'P'
            })
        nodes.remove(cur_node)
        nodes.reverse()
        return None, nodes, facts, result
        
