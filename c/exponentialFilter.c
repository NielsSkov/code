// Current
x[2] = pos_msg->xbd;
y[1] = x[2];

alpha = 0.01;
y[1] = alpha*y[1] + (1-alpha)*y_old;
y_old = y[1];

