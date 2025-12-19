let editorInstance;
let authToken = localStorage.getItem("admin_token") || null;

async function ensureAuth() {
  if (!authToken) {
    authToken = prompt("Paste admin Bearer token (from /token response) or cancel to continue read-only:");
    if (authToken) localStorage.setItem("admin_token", authToken);
  }
}

document.addEventListener("DOMContentLoaded", async () => {
  await ensureAuth();

  const select = document.getElementById("activity-select");
  const saveBtn = document.getElementById("save-btn");
  const msg = document.getElementById("admin-message");

  // initialize editor
  ClassicEditor.create(document.getElementById("editor")).then((editor) => {
    editorInstance = editor;
  });

  async function fetchActivities() {
    const res = await fetch("/activities");
    const activities = await res.json();
    select.innerHTML = "<option value=''>-- Select an activity --</option>";
    Object.keys(activities).forEach((name) => {
      const opt = document.createElement("option");
      opt.value = name;
      opt.textContent = name;
      select.appendChild(opt);
    });
    return activities;
  }

  const activities = await fetchActivities();

  select.addEventListener("change", (e) => {
    const name = select.value;
    if (!name) return;
    const desc = activities[name].description || "";
    if (editorInstance) editorInstance.setData(desc);
  });

  saveBtn.addEventListener("click", async () => {
    const name = select.value;
    if (!name) {
      msg.textContent = "Select an activity first";
      msg.className = "error";
      msg.classList.remove("hidden");
      return;
    }
    const description = editorInstance.getData();

    try {
      const res = await fetch(`/activities/${encodeURIComponent(name)}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          ...(authToken ? { Authorization: `Bearer ${authToken}` } : {}),
        },
        body: JSON.stringify({ description }),
      });
      if (!res.ok) {
        const j = await res.json();
        throw new Error(j.detail || "Failed to save");
      }
      msg.textContent = "Saved successfully";
      msg.className = "success";
      msg.classList.remove("hidden");
      setTimeout(() => msg.classList.add("hidden"), 3000);
    } catch (err) {
      msg.textContent = err.message;
      msg.className = "error";
      msg.classList.remove("hidden");
    }
  });
});
