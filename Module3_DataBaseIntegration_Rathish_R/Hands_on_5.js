// ============================================================
// TASK 1 — Create the Collection and Insert Documents
// ============================================================

use college_nosql;

db.feedback.insertMany([
    {
        student_id: 1,
        course_code: 'CS101',
        semester: '2022-ODD',
        rating: 5,
        comments: 'Excellent teaching. Would recommend.',
        tags: ['challenging', 'well-structured', 'good-examples'],
        submitted_at: ISODate('2022-11-30T10:15:00Z'),
        attachments: [{ filename: 'notes.pdf', size_kb: 240 }]
    },
    {
        student_id: 2,
        course_code: 'CS101',
        semester: '2022-ODD',
        rating: 4,
        comments: 'Good pace, clear explanations.',
        tags: ['well-structured', 'good-examples'],
        submitted_at: ISODate('2022-11-28T09:00:00Z'),
        attachments: [{ filename: 'slides.pdf', size_kb: 510 }]
    },
    {
        student_id: 3,
        course_code: 'CS101',
        semester: '2022-ODD',
        rating: 2,
        comments: 'Too fast, hard to keep up.',
        tags: ['challenging'],
        submitted_at: ISODate('2022-11-29T14:30:00Z'),
        attachments: [{ filename: 'doubts.pdf', size_kb: 80 }]
    },
    {
        student_id: 4,
        course_code: 'CS102',
        semester: '2022-ODD',
        rating: 5,
        comments: 'Best course this semester.',
        tags: ['well-structured', 'engaging'],
        submitted_at: ISODate('2022-11-27T11:00:00Z'),
        attachments: [{ filename: 'project.pdf', size_kb: 320 }]
    },
    {
        student_id: 5,
        course_code: 'CS102',
        semester: '2022-ODD',
        rating: 3,
        comments: 'Average, could use more examples.',
        tags: ['needs-examples'],
        submitted_at: ISODate('2022-11-26T16:45:00Z'),
        attachments: [{ filename: 'feedback.pdf', size_kb: 150 }]
    },
    {
        student_id: 6,
        course_code: 'MA101',
        semester: '2022-ODD',
        rating: 4,
        comments: 'Solid foundation course.',
        tags: ['well-structured'],
        submitted_at: ISODate('2022-11-25T08:30:00Z'),
        attachments: [{ filename: 'notes.pdf', size_kb: 190 }]
    },
    {
        student_id: 7,
        course_code: 'EC101',
        semester: '2021-EVEN',
        rating: 1,
        comments: 'Very confusing, needs restructuring.',
        tags: ['challenging', 'needs-examples'],
        submitted_at: ISODate('2021-05-15T13:00:00Z'),
        attachments: [{ filename: 'complaint.pdf', size_kb: 60 }]
    },
    {
        student_id: 8,
        course_code: 'ME101',
        semester: '2021-EVEN',
        rating: 3,
        comments: 'Decent but outdated material.',
        tags: ['needs-examples'],
        submitted_at: ISODate('2021-05-10T10:00:00Z'),
        attachments: [{ filename: 'syllabus.pdf', size_kb: 100 }]
    },
    {
        student_id: 9,
        course_code: 'CS101',
        semester: '2022-ODD',
        rating: 5,
        comments: 'Loved every lecture.',
        tags: ['challenging', 'engaging', 'well-structured'],
        submitted_at: ISODate('2022-12-01T09:15:00Z'),
        attachments: [{ filename: 'highlights.pdf', size_kb: 410 }]
    },
    {
        student_id: 10,
        course_code: 'CS102',
        semester: '2022-ODD',
        rating: 2,
        comments: 'Needs better assignments.',
        tags: ['needs-examples', 'challenging']
        // attachments field intentionally omitted — schema-less flexibility
    }
]);

db.feedback.countDocuments();


// ============================================================
// TASK 2 — CRUD Operations
// ============================================================

db.feedback.find({ rating: 5 });

db.feedback.find({
    course_code: 'CS101',
    tags: 'challenging'
});

db.feedback.find(
    {},
    { student_id: 1, course_code: 1, rating: 1, _id: 0 }
);

db.feedback.updateMany(
    { rating: { $lt: 3 } },
    { $set: { needs_review: true } }
);

db.feedback.updateMany(
    { needs_review: true },
    { $push: { tags: 'reviewed' } }
);

db.feedback.deleteMany({ semester: '2021-EVEN' });


// ============================================================
// TASK 3 — Aggregation Pipeline
// ============================================================

db.feedback.aggregate([
    { $match: { semester: '2022-ODD' } },
    {
        $group: {
            _id: '$course_code',
            avg_rating: { $avg: '$rating' },
            total_feedback: { $sum: 1 }
        }
    },
    { $sort: { avg_rating: -1 } }
]);

db.feedback.aggregate([
    { $match: { semester: '2022-ODD' } },
    {
        $group: {
            _id: '$course_code',
            avg_rating: { $avg: '$rating' },
            total_feedback: { $sum: 1 }
        }
    },
    {
        $project: {
            _id: 0,
            course_code: '$_id',
            average_rating: { $round: ['$avg_rating', 1] },
            total_feedback: 1
        }
    },
    { $sort: { average_rating: -1 } }
]);

db.feedback.aggregate([
    { $unwind: '$tags' },
    {
        $group: {
            _id: '$tags',
            count: { $sum: 1 }
        }
    },
    { $sort: { count: -1 } }
]);

db.feedback.createIndex({ course_code: 1 });

db.feedback.find({ course_code: 'CS101' }).explain('executionStats');
