# laboratory work #3 for Decision theory

train_document = open('1.txt', 'r')

boxes = []
for i in train_document:
    for box in i.split():
        boxes.append(int(box))

train_document.close()

print "********"
print "DATA: {}".format(boxes)

containers = [[]]
containers_count = 0
container_capacity = 100
sum_container = 0

for box in boxes:
    sum_container += int(box)
    if sum_container <= container_capacity:
        containers[containers_count].append(box)
    else:
        sum_container = int(box)
        containers.append([])
        containers_count += 1
        containers[containers_count].append(box)
    # print sum_container

print "********"
print "NFA: {}".format(containers)

containers = [[]]
containers_count = 0
containers_weight = [0]

for box in boxes:
    if (containers_weight[containers_count] + box) <= container_capacity:
        containers[containers_count].append(box)
        containers_weight[containers_count] += box
        # print "Containers_weight: {}".format(containers_weight)
    else:
        placed = False
        for i in range(containers_count):
            if (containers_weight[i] + box) <= container_capacity:
                containers[i].append(box)
                containers_weight[i] += box
                # print "Containers_weight: {}".format(containers_weight)
                placed = True
                break
        if not placed:
            containers.append([])
            containers_count += 1
            containers[containers_count].append(box)
            containers_weight.append(box)
    # print containers

print "********"
print "FFA: {}".format(containers)


containers = [[]]
containers_count = 0
containers_weight = [0]

for box in boxes:
    if (containers_weight[containers_count] + box) <=container_capacity:
        containers[containers_count].append(box)
        containers_weight[containers_count] += box
    else:
        min_weight = min(containers_weight)
        min_index = containers_weight.index(min_weight)
        # print "Min index: {}".format(min_index)
        if( min_weight + box ) <= container_capacity:
            containers[min_index].append(box)
            containers_weight[min_index] += box
        else:
            containers.append([])
            containers_count += 1
            containers[containers_count].append(box)
            containers_weight.append(box)

print "********"
print "WFA: {}".format(containers)

containers = [[]]
containers_count = 0
containers_weight = [0]

for box in boxes:
    if (containers_weight[containers_count] + box) <= container_capacity:
        containers[containers_count].append(box)
        containers_weight[containers_count] += box
    else:
        placed = False
        find_max = list(containers_weight)
        find_max[containers_count] = 0
        # print find_max
        for iter in range(containers_count):
            max_weight = max(find_max)
            # print "max_weight: {}".format(max_weight)
            max_index = containers_weight.index(max_weight)
            # print "max_index: {}".format(max_index)
            if max_weight + box <= container_capacity:
                containers[max_index].append(box)
                containers_weight[max_index] += box
                placed = True
                break
            else:
                find_max[max_index] = 0
                # print find_max
        if not placed:
            containers.append([])
            containers_count += 1
            containers[containers_count].append(box)
            containers_weight.append(box)

print "********"
print "BFA: {}".format(containers)