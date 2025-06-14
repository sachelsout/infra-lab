from flask import Flask, request, redirect
import redis
import os

app = Flask(__name__)

# Redis connection
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Set limit from form submission
    if request.method == 'POST':
        limit = request.form.get('limit')
        if limit and limit.isdigit():
            r.set('limit', int(limit))
    
    # Get current count and limit
    count = int(r.get('count') or 0)
    limit = r.get('limit')
    limit_str = limit if limit else '∞'

    # Check if count exceeds limit
    if limit:
        limit = int(limit)
        if count >= limit:
            return f"""
            <h2>⚠️ Limit of {limit} reached!</h2>
            <form method="POST">
                <label>Set new limit:</label>
                <input type="number" name="limit">
                <button type="submit">Update</button>
            </form>
            <br><a href="/reset">🔄 Reset Counter</a>
            """

    # Increment and save count
    count += 1
    r.set('count', count)

    return f"""
    <h2>✅ Counter: {count} (Limit: {limit_str})</h2>
    <form method="POST">
        <label>Set limit:</label>
        <input type="number" name="limit">
        <button type="submit">Submit</button>
    </form>
    <br><a href="/reset">🔄 Reset Counter</a>
    """

@app.route('/reset')
def reset():
    r.delete('count')
    r.delete('limit')
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
