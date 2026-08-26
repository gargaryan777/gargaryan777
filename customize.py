#!/usr/bin/env python3
import json
import os
import re

def main():
    config_path = "config.json"
    if not os.path.exists(config_path):
        print(f"Error: {config_path} not found! Please make sure it exists in the workspace.")
        return

    with open(config_path, "r") as f:
        config = json.load(f)

    # Required configuration fields
    username = config.get("github_username", "gargaryan777")
    full_name = config.get("full_name", "Aryan Garg")
    email = config.get("email", "gargaryan52@gmail.com")
    role = config.get("role", "Full-Stack Developer")
    origin = config.get("origin", "Jaipur, India")
    education = config.get("education", "B.Tech in Computer Science")
    status = config.get("status", "Building + Learning + Shipping")
    toolchain = config.get("toolchain", "VS Code, Git, Figma, Postman")
    core_lang = config.get("core_lang", "TypeScript, JavaScript, Python, C++")
    core_frontend = config.get("core_frontend", "React, Next.js, HTML/CSS, Tailwind")
    core_backend = config.get("core_backend", "Node.js, Express, FastAPI")
    core_database = config.get("core_database", "PostgreSQL, MongoDB, Redis")
    core_infra = config.get("core_infra", "Vercel, Docker, AWS, GitHub Actions")
    linkedin = config.get("linkedin", "aryan-garg-dev")
    instagram = config.get("instagram", "aryan_garg")
    facebook = config.get("facebook", "gargaryan777")

    print(f"Customizing profile repository for user '{username}' ({full_name})...")

    # 1. Update dark.svg and light.svg
    svg_files = ["dark.svg", "light.svg"]
    for svg_file in svg_files:
        if os.path.exists(svg_file):
            print(f"Customizing {svg_file}...")
            with open(svg_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Perform string replacements for the terminal display
            content = content.replace("arifhasan.connect@gmail.com", email)
            content = content.replace("Arif Hasan", full_name)
            content = content.replace("Full-Stack Developer", role)
            content = content.replace("Sylhet, Bangladesh", origin)
            content = content.replace("BSc in CSE", education)
            content = content.replace("Building + Learning + Shipping", status)
            content = content.replace("VS Code, Git, Android Studio, Figma", toolchain)
            content = content.replace("Dart, C++, Python", core_lang)
            content = content.replace("Flutter", core_frontend)
            content = content.replace("Node.js", core_backend)
            content = content.replace("Firebase, MongoDB", core_database)
            content = content.replace("Vercel, Docker, Git", core_infra)
            content = content.replace("@arifhaxn", f"@{username}")
            content = content.replace("@arifhaxnn", f"@{facebook}")
            content = content.replace("arif-hasan-672249358", linkedin)

            with open(svg_file, "w", encoding="utf-8") as f:
                f.write(content)

    # 2. Update README.md
    readme_file = "README.md"
    if os.path.exists(readme_file):
        print(f"Customizing {readme_file}...")
        with open(readme_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Replace arifhaxn references
        content = content.replace("arifhaxn", username)
        # Replace other contact references
        content = content.replace("arif-hasan-672249358", linkedin)
        content = content.replace("arifhasnn", facebook)

        # Replace arifhaxn's email address in the hero banner of the README.md
        content = content.replace("arifhasan2002@gmail.com", email)

        with open(readme_file, "w", encoding="utf-8") as f:
            f.write(content)

    # 3. Update projects.json
    projects_file = "projects.json"
    if os.path.exists(projects_file):
        print(f"Customizing {projects_file}...")
        with open(projects_file, "r", encoding="utf-8") as f:
            projects = json.load(f)

        for p in projects:
            # Replace author name in repo paths
            p["repo"] = p.get("repo", "").replace("arifhaxn", username)

        with open(projects_file, "w", encoding="utf-8") as f:
            json.dump(projects, f, indent=2)

    # 4. Update workflow files
    workflows = [".github/workflows/projects.yml", ".github/workflows/snake.yml"]
    for wf in workflows:
        if os.path.exists(wf):
            print(f"Customizing {wf}...")
            with open(wf, "r", encoding="utf-8") as f:
                content = f.read()

            content = content.replace("arifhaxn", username)

            with open(wf, "w", encoding="utf-8") as f:
                f.write(content)

    print("\nCustomization complete! All templates updated successfully.")

if __name__ == "__main__":
    main()
