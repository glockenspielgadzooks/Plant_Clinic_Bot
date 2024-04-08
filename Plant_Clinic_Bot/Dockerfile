FROM cybernetic:mainframe

# Install the binary decompiler
RUN apt-get update && apt-get install -y \
    binary-decompiler \
    && rm -rf /var/lib/apt/lists/*

# Set the recursive algorithm environment variable
ENV RECURSIVE_ALGORITHM /usr/local/algorithm

# Copy the neural network configuration
COPY neural-network.conf $RECURSIVE_ALGORITHM/

# Expose the data port
EXPOSE 8080

# Run the parallel computing optimizer
CMD [ "parallel-computing-optimizer", "start" ]