# CLAUDE.md - AI Assistant Guide for outbreak-activity

**Last Updated**: 2025-12-10
**Repository**: outbreak-activity
**Purpose**: Interactive outbreak investigation simulation exercise featuring interviews, sample collection, and line list creation

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Codebase Architecture](#codebase-architecture)
3. [Directory Structure](#directory-structure)
4. [Application Details](#application-details)
5. [Development Workflows](#development-workflows)
6. [Key Conventions](#key-conventions)
7. [Working with this Codebase](#working-with-this-codebase)
8. [Testing and Serving](#testing-and-serving)
9. [Best Practices for AI Assistants](#best-practices-for-ai-assistants)

---

## Project Overview

This repository contains a **multi-app static HTML workspace** for educational outbreak investigation simulations. The project consists of three main interactive web applications:

1. **Dialogue Editor** - Visual JSON editor for creating branching dialogue scenarios
2. **Dialogue Player** - Interactive player for dialogue scenarios with decision tracking and analytics
3. **Seat/Sample Designer** - Visual editor for spatial layouts (seating charts, sample collection maps)

### Key Characteristics

- **No Build System**: Pure static HTML/CSS/JavaScript files
- **No Dependencies**: Vanilla JavaScript, no npm packages required
- **Self-Contained**: Each app is a single HTML file with inline styles and scripts
- **Educational Purpose**: Designed for outbreak investigation training and simulation

---

## Codebase Architecture

### Wrapper + Template Pattern

The repository uses a **two-tier architecture**:

```
apps/
├── [app-name]/
│   └── index.html          (350-750 bytes) - Lightweight wrapper
└── template/
    └── [app-name].html     (30-74 KB) - Full implementation
```

**How it Works**:
- Each app folder contains a minimal wrapper `index.html`
- The wrapper loads the actual app via iframe from `apps/template/[app-name].html`
- This provides **single source of truth** - update one file, all instances update

**Benefits**:
- DRY (Don't Repeat Yourself) - no code duplication
- Easy maintenance - edit once in template
- Flexible routing - each app accessible at its own path
- Relative URLs work from different server roots

**Example Wrapper**:
```html
<!doctype html>
<html>
<head><title>App Name</title></head>
<body style="margin:0;overflow:hidden">
  <iframe src="/apps/template/app-name.html"
          style="border:0;width:100%;height:100vh">
  </iframe>
</body>
</html>
```

---

## Directory Structure

```
outbreak-activity/
├── index.html              # Root landing page with app directory
├── package.json            # npm scripts (optional, no dependencies)
├── serve.sh                # Shell script to start Python HTTP server
├── serve_dynamic.py        # Python server with dynamic index generation
├── README.md               # Basic project description
├── WORKSPACE.md            # Multi-app workspace documentation
├── CLAUDE.md               # This file - AI assistant guide
├── .gitignore              # Git ignore patterns
│
└── apps/                   # All web applications
    ├── dialogue-editor/
    │   └── index.html      # (405 bytes) Wrapper → template
    ├── dialogue-player/
    │   └── index.html      # (747 bytes) Wrapper → template
    ├── seat-sample-designer/
    │   └── index.html      # (343 bytes) Wrapper → template
    │
    └── template/           # MASTER FILES - single source of truth
        ├── index.html                      # Template info page
        ├── dialogue-editor.html            # (44.9 KB) Full editor
        ├── dialogue-player.html            # (73.6 KB) Full player
        └── seat-sample-designer.html       # (30.5 KB) Full designer
```

### Critical Directories

- **`apps/template/`** - Primary development location for all app code
- **`apps/[app-name]/`** - Wrappers only, rarely need modification
- **Root** - Server configuration, landing page, documentation

---

## Application Details

### 1. Dialogue Editor (`apps/template/dialogue-editor.html`)

**Purpose**: Create interactive branching dialogue scenarios with choices, effects, and game mechanics

**Key Features**:
- Node-based dialogue system with speakers and text
- Multiple choice support with branching paths
- **Effects System**:
  - Approval effects (character relationship tracking)
  - Stat effects (traits/attributes)
- Visual node list with status indicators
- Real-time JSON preview
- Import/Export JSON functionality
- Keyboard shortcuts (Ctrl+S, Ctrl+N)

**Data Structure**:
```javascript
{
  title: "Scenario Name",
  startNode: "node_id",
  approvalTypes: [
    { id: "approval_1", name: "Political Approval", initial: 50 }
  ],
  nodes: [
    {
      id: "unique_id",
      speaker: "Character Name",
      text: "Dialogue text",
      next: "next_node_id",  // For linear progression
      choices: [             // For branching
        {
          text: "Player choice text",
          next: "target_node_id",
          effects: {
            approvals: { approval_id: +10 },
            stats: { trait_name: 5 }
          }
        }
      ]
    }
  ]
}
```

**UI Layout**: 3-column grid
- Left sidebar (280px): Node list
- Center (flex): Main editor
- Right panel (320px): Approvals + JSON preview

**Technologies**: Vanilla JS, CSS Grid, CSS Variables

---

### 2. Dialogue Player (`apps/template/dialogue-player.html`)

**Purpose**: Interactive player for dialogue scenarios with comprehensive analytics

**Key Features**:
- **Game State Management**: Track current node, history, stats, approvals
- **Navigation**: Back/forward through history
- **Card Marking**: Mark nodes as "?" (Question) or "!" (Decision)
- **Analytics**:
  - Decision count tracking
  - Time elapsed
  - Path taken with effects
- **Reporting**:
  - End summary modal with stats
  - Full decision report with path visualization
  - Final scores display
- **Decision Tree Visualization**:
  - SVG-based hierarchical tree
  - Pan (space+drag) and zoom (mousewheel)
  - Highlighted taken path
  - Hover tooltips with full node details
  - Visual encoding for question/decision types
- **Accessibility**:
  - Keyboard shortcuts (1-9 for choices, arrows for history, ESC for modals)
  - Font size toggle
  - Dark/Light theme toggle

**State Structure**:
```javascript
{
  dialogueData: {},      // Loaded JSON
  currentNodeId: "",     // Active node
  history: [],           // Navigation history
  historyIndex: -1,      // Position in history
  stats: {},             // Custom stats
  approvals: {},         // Approval ratings
  startTime: null,       // Session start
  decisionCount: 0,      // Choices made
  questionCount: 0,      // Questions marked
  decisionTypeCount: 0,  // Decisions marked
  gameEnded: false,      // Session status
  pathTaken: [],         // Full path with effects
  nodeCardTypes: {}      // User markings per node
}
```

**UI Sections**:
- Header: Title, file upload, reset, font/theme toggles
- Main: Dialogue display, choices, navigation
- Sidebar: Progress panel, history list
- Modals: Reveal summary, full report, decision tree

**Technologies**: Vanilla JS, SVG Canvas, CSS Animations

---

### 3. Seat/Sample Designer (`apps/template/seat-sample-designer.html`)

**Purpose**: Visual spatial layout editor for seating arrangements or sample collection mapping

**Key Features**:
- **Drawing Modes**:
  - Select/Move/Drag
  - Draw polygon sections (multi-click vertices)
  - Add individual players/samples
  - Delete selected elements
- **Grid System**: Snap-to-grid with adjustable grid size (5-100px)
- **Selection**: Click, multi-select (shift), box-select (drag)
- **Pan & Zoom**:
  - Space+drag to pan
  - Mousewheel to zoom
  - Zoom controls (+, -, Reset)
- **Properties Panel**:
  - **Sections**: ID, name, color
  - **Players**: Section assignment, name, age, alive/deceased status, symptomatic flag, medical history, custom color
- **Import/Export JSON**

**Data Structure**:
```javascript
{
  config: {
    hover_metrics: ["total_count", "percent_deceased", "percent_symptomatic"]
  },
  sections: [
    {
      id: "section_1",
      name: "Section Name",
      color: "#4facfe",
      polygon_points: "x1,y1 x2,y2 x3,y3",  // Space-separated pairs
      label_pos: { x: centerX, y: centerY }
    }
  ],
  players: [
    {
      id: 1,
      section_id: "section_1",
      x: 100, y: 100,
      name: "Player 1",
      age: 30,
      alive: true,
      symptomatic: false,
      history: "Medical history text",
      custom_color: "#ffffff"  // Optional override
    }
  ]
}
```

**Coordinate System**: SVG local coordinates with viewport transformation
- Screen to local: `(Screen - Translate) / Scale`
- Grid snapping rounds to nearest grid unit

**Technologies**: SVG Canvas, Vanilla JS, Geometric Calculations

---

## Development Workflows

### Adding a New App

1. **Copy Template**:
   ```bash
   cp -r apps/template apps/my-new-app
   # Edit apps/my-new-app/index.html
   ```

2. **Create Wrapper** (in `apps/my-new-app/index.html`):
   ```html
   <!doctype html>
   <html>
   <head><title>My New App</title></head>
   <body style="margin:0;overflow:hidden">
     <iframe src="/apps/template/my-new-app.html"
             style="border:0;width:100%;height:100vh">
     </iframe>
   </body>
   </html>
   ```

3. **Create Implementation** (in `apps/template/my-new-app.html`):
   - Self-contained HTML file
   - Inline CSS in `<style>` tags
   - Inline JavaScript in `<script>` tags
   - No external dependencies

4. **Update Root Index** (`index.html`):
   - Add card linking to new app

### Modifying Existing Apps

**IMPORTANT**: Always edit files in `apps/template/`, NOT in individual app folders.

**Workflow**:
1. Identify the app to modify
2. Edit `apps/template/[app-name].html`
3. Test changes by accessing app via any route
4. Changes immediately reflect in all wrappers

**Example**: To fix a bug in Dialogue Editor:
- Edit: `apps/template/dialogue-editor.html`
- Test: `http://localhost:8000/apps/dialogue-editor/`

### Git Workflow

**Current Branch**: `claude/claude-md-mj00izt2oi1hcqth-012g24KPLaWm8ageS9vHfsmn`

**Key Practices**:
1. Develop on designated branch
2. Commit with clear, descriptive messages
3. Push to specified branch when complete
4. Never push to main/master without permission
5. Use relative file paths in commits

**Recent Commits**:
```
0bf5b98 - fix(index): use relative app links so apps open when served from different roots
b40f161 - chore(workspace): add dynamic index server; update serve.sh and package.json
0c0f6fd - chore(workspace): add root index listing available apps
c279edb - chore(workspace): scaffold multi-app static apps; add template, app wrappers, serve script, README update, .gitignore
5f10b78 - Initial commit
```

**Commit Message Style**:
- Use conventional commits: `type(scope): description`
- Types: `feat`, `fix`, `chore`, `docs`, `refactor`
- Scopes: `workspace`, `index`, app names, etc.
- Keep first line under 72 characters

---

## Key Conventions

### File Naming

- **Kebab-case** for directories: `dialogue-editor`, `seat-sample-designer`
- **Kebab-case** for HTML files: `dialogue-editor.html`
- **snake_case** for Python scripts: `serve_dynamic.py`
- **README/CLAUDE/WORKSPACE** in uppercase for documentation

### Code Style

**HTML**:
- Use semantic HTML5 tags
- Include `lang="en"` on `<html>` tag
- Use `utf-8` charset
- Include viewport meta tag for responsiveness

**CSS**:
- Use CSS variables for theming (`:root { --bg: #0f1720; }`)
- Prefer CSS Grid and Flexbox for layouts
- Use relative units (rem, em, %) when appropriate
- Include hover states and transitions for interactivity
- Dark theme as default

**JavaScript**:
- Vanilla JavaScript (no frameworks)
- Avoid global namespace pollution (use IIFE or modules)
- Use `const`/`let`, avoid `var`
- Clear function and variable names
- Inline comments for complex logic

### Data Formats

**JSON Export/Import**:
- Pretty-printed JSON (2-space indent)
- Use descriptive property names
- Include metadata (title, version if applicable)
- Validate on import

**Coordinates**:
- Use numeric values (not strings)
- SVG local coordinates (not screen pixels)
- Include both x and y explicitly

**Colors**:
- Hex format: `#4facfe`
- Include opacity in hex when needed: `#4facfe80`
- Use CSS variables for theme colors

---

## Testing and Serving

### Starting the Development Server

**Option 1: Shell Script** (Recommended, no Node.js required)
```bash
chmod +x serve.sh
./serve.sh              # Default port 8000
./serve.sh 8080         # Custom port
./serve.sh dynamic      # Use dynamic index (serve_dynamic.py)
./serve.sh dynamic 8080 # Dynamic index on port 8080
```

**Option 2: npm Scripts** (If Node.js installed)
```bash
npm run start           # Port 8000
npm run start:port      # Port 8080
npm run start:dynamic   # Dynamic index
```

### Accessing Applications

**Root Index**: `http://localhost:8000/`
- Landing page with links to all apps

**Individual Apps**:
- Dialogue Editor: `http://localhost:8000/apps/dialogue-editor/`
- Dialogue Player: `http://localhost:8000/apps/dialogue-player/`
- Seat/Sample Designer: `http://localhost:8000/apps/seat-sample-designer/`
- Template: `http://localhost:8000/apps/template/`

### Testing Workflows

**Manual Testing**:
1. Start server
2. Open browser to app URL
3. Test features interactively
4. Verify data export/import
5. Test on different browsers (Chrome, Firefox, Safari)
6. Test responsive behavior (resize window)

**File Operations Testing**:
- Export JSON → Verify format and content
- Import JSON → Verify data restoration
- Copy to clipboard → Test in different scenarios

**Interaction Testing**:
- Click interactions
- Keyboard shortcuts
- Drag and drop (Seat Designer)
- Pan and zoom (Dialogue Player tree, Seat Designer)
- Form inputs and validation

---

## Working with this Codebase

### File Reading Strategy

**When Modifying Apps**:
1. Always read `apps/template/[app-name].html` first
2. Understand the full file structure before editing
3. Locate the specific section to modify
4. Test changes by serving locally

**File Sizes** (be aware for context limits):
- `dialogue-editor.html`: ~45 KB, ~1,318 lines
- `dialogue-player.html`: ~74 KB, ~1,730 lines
- `seat-sample-designer.html`: ~30 KB, ~756 lines

**Tip**: Use line numbers when reading to navigate efficiently.

### Common Modification Patterns

**Adding a Feature to an App**:
1. Read the template file: `Read apps/template/[app-name].html`
2. Locate relevant section (HTML structure, CSS styles, or JS functions)
3. Use `Edit` tool with precise `old_string` matching
4. Test changes locally
5. Commit with descriptive message

**Fixing a Bug**:
1. Understand the bug by reading code
2. Locate the buggy section
3. Edit with minimal changes
4. Test fix thoroughly
5. Commit with `fix(app-name): description`

**Updating Styles**:
1. Locate CSS section in template file
2. Modify CSS variables or specific rules
3. Test visual changes in browser
4. Ensure responsive behavior maintained

### Data Flow Understanding

**Dialogue Editor → Dialogue Player**:
```
1. Create dialogue in Editor
2. Export JSON file
3. Import JSON in Player
4. Play scenario
5. View analytics and reports
```

**Seat/Sample Designer**:
```
1. Draw sections with polygon tool
2. Place players/samples
3. Edit properties in sidebar
4. Export JSON for analysis
5. Import JSON to restore layout
```

### Common Pitfall Avoidance

**❌ Don't**:
- Edit wrapper files in `apps/[app-name]/index.html` (unless changing iframe src)
- Add external dependencies (npm packages, CDN scripts)
- Create build processes or transpilation
- Modify files outside of `apps/template/` for app changes
- Use absolute paths in URLs (breaks when served from different roots)

**✅ Do**:
- Edit template files in `apps/template/`
- Keep code self-contained in single HTML files
- Use inline styles and scripts
- Test changes by serving locally
- Use relative paths in links: `href="apps/dialogue-editor/"`
- Maintain the wrapper + template pattern

---

## Best Practices for AI Assistants

### General Principles

1. **Always Read Before Editing**
   - Never propose changes without reading the target file first
   - Understand the full context before modifications

2. **Respect the Architecture**
   - Maintain the wrapper + template pattern
   - Don't introduce build systems or external dependencies
   - Keep apps as self-contained single HTML files

3. **Minimal Changes**
   - Make only the requested changes
   - Avoid over-engineering or premature optimization
   - Don't refactor unrelated code

4. **Test Awareness**
   - Remind users to test changes locally
   - Provide serving instructions when relevant
   - Note which app(s) are affected by changes

### File Operations

**Reading Files**:
```
Priority: apps/template/[app-name].html (not wrapper files)
```

**Editing Files**:
```
Target: apps/template/[app-name].html
Tool: Edit with precise old_string matching
Preserve: Indentation, line breaks, code style
```

**Creating Files**:
```
Only when: Adding entirely new app
Location: apps/template/ for implementation
          apps/[new-app]/ for wrapper
```

### Specific Guidance by Task Type

**Adding Features**:
1. Read relevant template file completely
2. Identify insertion point for new code
3. Add HTML structure if needed
4. Add CSS styles in `<style>` section
5. Add JavaScript in `<script>` section
6. Maintain existing code style and patterns
7. Test locally before committing

**Bug Fixes**:
1. Understand the bug thoroughly
2. Locate the problematic code section
3. Make minimal, targeted fix
4. Verify fix doesn't break other functionality
5. Commit with clear description of issue and fix

**Style Updates**:
1. Locate CSS section in template file
2. Modify only necessary rules/variables
3. Maintain color scheme consistency
4. Test responsive behavior
5. Ensure accessibility maintained

**Data Structure Changes**:
1. Understand current data structure
2. Update JavaScript data handling
3. Update UI to reflect new structure
4. Ensure import/export compatibility
5. Consider backwards compatibility if relevant

### Communication Best Practices

**When Describing Changes**:
- Use file paths with line numbers: `apps/template/dialogue-editor.html:245`
- Be specific about which app is affected
- Mention if wrapper or template file was changed
- Provide before/after examples for complex changes

**When Suggesting Workflows**:
- Include full file paths
- Provide serving instructions
- Mention browser testing
- Note any keyboard shortcuts or interactions to test

**When Encountering Issues**:
- Read the full template file to understand context
- Check if issue is in wrapper vs template
- Verify changes are in the correct file
- Suggest local testing steps

### Code Quality Standards

**HTML**:
- Use semantic tags (`<main>`, `<section>`, `<article>`)
- Include ARIA labels for accessibility when appropriate
- Maintain proper nesting and indentation

**CSS**:
- Use CSS variables for colors and spacing
- Group related styles together
- Comment complex or non-obvious styles
- Maintain consistent naming conventions

**JavaScript**:
- Use descriptive variable and function names
- Add comments for complex logic
- Handle edge cases and errors gracefully
- Validate user input before processing
- Use modern ES6+ syntax (const/let, arrow functions, template literals)

### Security Considerations

**User Input**:
- Sanitize before rendering (avoid XSS)
- Validate file uploads (JSON structure)
- Handle malformed data gracefully

**JSON Import**:
- Validate structure before applying
- Handle parse errors with user-friendly messages
- Don't execute arbitrary code from imported data

---

## Quick Reference

### Key Files to Know

| File | Purpose | When to Edit |
|------|---------|--------------|
| `apps/template/dialogue-editor.html` | Dialogue editor implementation | Adding features, fixing bugs, styling |
| `apps/template/dialogue-player.html` | Dialogue player implementation | Game mechanics, analytics, visualization |
| `apps/template/seat-sample-designer.html` | Seat designer implementation | Drawing features, spatial logic |
| `index.html` | Root landing page | Adding new apps to directory |
| `serve.sh` | Development server script | Changing default port or serving behavior |
| `package.json` | npm scripts | Adding new convenience commands |
| `CLAUDE.md` | This guide | Documenting new conventions or workflows |

### Common Commands

```bash
# Start server (Python, no Node needed)
./serve.sh

# Start server on custom port
./serve.sh 8080

# Start with dynamic index
./serve.sh dynamic

# Via npm (if Node.js installed)
npm run start

# View files
ls apps/template/

# Check git status
git status

# Create new app
cp -r apps/template apps/my-app
```

### Architecture Cheat Sheet

```
User Request → App URL → Wrapper (index.html) →
    iframe → Template File (actual implementation)

Example:
http://localhost:8000/apps/dialogue-editor/
    ↓
apps/dialogue-editor/index.html (wrapper, 405 bytes)
    ↓
<iframe src="/apps/template/dialogue-editor.html">
    ↓
apps/template/dialogue-editor.html (implementation, 44.9 KB)
```

---

## Conclusion

This repository provides a clean, minimal architecture for hosting multiple static HTML educational apps. The wrapper + template pattern ensures maintainability while the no-build-system approach keeps deployment simple.

**Key Takeaways for AI Assistants**:
- Edit templates in `apps/template/`, not wrappers
- Maintain self-contained single-file apps
- Respect the no-dependencies, vanilla JavaScript approach
- Always read files before proposing changes
- Test locally by serving and accessing apps in browser
- Follow existing code style and conventions

**Questions or Issues?**
Refer to WORKSPACE.md for multi-app workspace documentation, or examine the template files directly for implementation details.

---

**Document Version**: 1.0
**Generated**: 2025-12-10
**Maintainer**: AI-generated documentation for AI assistants
