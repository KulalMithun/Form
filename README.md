<h1>Anonymous Form with Admin Dashboard</h1>

<p>I created this project for my self learning. It is a simple, small, dynamic <strong>anonymous form</strong> designed especially for <strong>anti-ragging committees</strong> or similar use-cases where users can submit reports without logging in.</p>

<hr>

<h2>🌟 Features</h2>
<ul>
  <li>📄 Anonymous form submission without login</li>
  <li>🛡️ Admin authentication to view submitted reports</li>
  <li>📊 Real-time dashboard to view submissions</li>
  <li>📁 Google Sheets integration – all submissions are automatically saved</li>
  <li>📥 Small, Secure and Swift</li>
</ul>

<hr>

<h2>📌 What It Does</h2>
<ul>
  <li>Users can scan a QR or visit the website and submit a form anonymously.</li>
  <li>The data (name and issue) is directly saved to a Google Sheet in real-time.</li>
  <li>Admins can log in via a secure login page and view all submissions in a dashboard.</li>
</ul>

<hr>

<h2>🔐 Default Login Details</h2>

<p>
  The default admin credentials are:
  <br><strong>Username:</strong> <code>admin</code>
  <br><strong>Password:</strong> <code>adminpass</code>
</p>

<p>
  You can <strong>change these credentials</strong> securely while deploying the app by setting the following environment variables:
</p>

<ul>
  <li><code>ADMIN_USERNAME</code></li>
  <li><code>ADMIN_PASSWORD</code></li>
</ul>

<hr>

<h2>📷 Screenshots</h2>

<p><img src="https://github.com/KulalMithun/Form/blob/main/Screenshot%202025-07-03%20061646.png" width="500"></p>
<p><img src="https://github.com/KulalMithun/Form/blob/main/Screenshot%202025-07-03%20061754.png" width="500"></p>

<hr>

<h2>🚀 Deploy to Render</h2>

<p>One-click deploy on Render using the button below:</p>

<p>
  <a href="https://render.com/deploy?repo=https://github.com/KulalMithun/Form">
    <img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render">
  </a>
</p>

<hr>

<h2>⚙️ Setup Instructions</h2>

<ol>
  <li>Clone this repo</li>
  <li>Create a <code>creds.json</code> file by enabling Google Sheets API and Google Drive API</li>
  <li>Share your Google Sheet with the service account email (from creds.json)</li>
  <li>Update your <code>app.py</code> to match your Google Sheet ID</li>
  <li>Set <code>ADMIN_USERNAME</code> and <code>ADMIN_PASSWORD</code> as environment variables on Render</li>
</ol>

<hr>

<h2>📁 Data Storage</h2>
<ul>
  <li>All form submissions are saved in a Google Sheet as CSV format</li>
  <li>CSV data is updated in real time and displayed live in the admin dashboard</li>
</ul>

<hr>

<h2>All Contribution are Accepted.</h2>

<h2>🧠 Author</h2>
<p>By <strong>Kulal Mithun</strong> — For learning, practice, and practical use by anti-ragging committees and educators.</p>
