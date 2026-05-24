<script lang="ts">
    import { goto } from '$app/navigation';
    import { TaskService } from '$lib/services/task-service';

    let { data } = $props();

    let title = $state(data.task.title);
    let description = $state(data.task.description ?? '');
    let status = $state(data.task.status);
    let dueDateTime = $state(data.task.due_date.slice(0, 16));

    let dueDate = $derived(dueDateTime ? `${dueDateTime}:00Z` : null);

    async function handleSubmit() {
        try {
            await TaskService.updateTask(data.task.id, { title, description, status, due_date: dueDate });
            goto(`/tasks/${data.task.id}`);
        } catch (error) {
            console.error('Error updating task:', error);
        }
    }

    function handleCancel() {
        goto(`/tasks/${data.task.id}`);
    }
</script>

{#if data.task}
    <div class="govuk-width-container">
        <a href="/tasks/{data.task.id}" class="govuk-back-link">Back</a>
        <fieldset class="govuk-fieldset">
            <legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
                <h1 class="govuk-fieldset__heading">Edit task</h1>
            </legend>
            <div class="govuk-form-group">
                <label class="govuk-label" for="task-title">Title</label>
                <input class="govuk-input" id="task-title" name="title" type="text" bind:value={title} />
            </div>
            <div class="govuk-form-group">
                <label class="govuk-label" for="task-description">Description (optional)</label>
                <textarea
                    class="govuk-textarea"
                    id="task-description"
                    name="description"
                    rows="5"
                    bind:value={description}
                ></textarea>
            </div>
            <div class="govuk-form-group">
                <label class="govuk-label" for="task-status">Status</label>
                <select class="govuk-select" id="task-status" name="status" bind:value={status}>
                    {#each data.taskStatuses as s}
                        <option value={s.value}>{s.label}</option>
                    {/each}
                </select>
            </div>
            <div class="govuk-form-group">
                <label class="govuk-label" for="task-due-date">Due date and time</label>
                <input
                    class="govuk-input govuk-input--width-20"
                    id="task-due-date"
                    name="dueDate"
                    type="datetime-local"
                    bind:value={dueDateTime}
                />
            </div>
            <div class="govuk-button-group">
                <button type="submit" class="govuk-button" data-module="govuk-button" onclick={handleSubmit}>
                    Save
                </button>
                <button type="button" class="govuk-button govuk-button--secondary" onclick={handleCancel}>
                    Cancel
                </button>
            </div>
        </fieldset>
    </div>
{:else}
    <div class="govuk-width-container">
        <div class="govuk-main-wrapper--auto-spacing" id="main-content" role="main">
            <h1 class="govuk-heading-xl">Task not found</h1>
            <p class="govuk-body">The task you are looking for does not exist.</p>
        </div>
    </div>
{/if}
