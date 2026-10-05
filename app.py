from flask import Flask, render_template, request, redirect, url_for, flash
from database import init_db, get_all_notes, search_notes, add_note, delete_note
import os

app = Flask(__name__)
# In production, use a secure random secret key. For educational purposes, a hardcoded one is ok, but we allow env override
app.secret_key = os.environ.get('SECRET_KEY', 'dev-sec-ops-educational-key')

# Initialize the database automatically when the app starts
init_db()

@app.route('/')
def index():
    search_query = request.args.get('search', '').strip()
    if search_query:
        notes = search_notes(search_query)
    else:
        notes = get_all_notes()
    return render_template('index.html', notes=notes, search_query=search_query)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title', '').strip()
    content = request.form.get('content', '').strip()
    
    if not title or not content:
        flash("Title and content are required.", "error")
        return redirect(url_for('index'))
    
    if len(title) > 100 or len(content) > 1000:
        flash("Title or content is too long.", "error")
        return redirect(url_for('index'))
        
    add_note(title, content)
    flash("Note created successfully.", "success")
    return redirect(url_for('index'))

@app.route('/delete/<int:note_id>', methods=['POST'])
def delete(note_id):
    delete_note(note_id)
    flash("Note deleted successfully.", "success")
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port, host='0.0.0.0')
