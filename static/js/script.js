function IncrementCounter() {
            fetch('/increment', { method: 'POST' })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('counter').textContent = data.counter;
                    // console.log(data);
                });
        }

function DecrementCounter() {
            fetch('/decrement', { method: 'POST'})
              .then(response => response.json())
              .then(data => {
                  document.getElementById('counter').textContent = data.counter;
                });
        }

// リファクタリング
